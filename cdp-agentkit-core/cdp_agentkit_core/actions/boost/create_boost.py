from collections.abc import Callable

from cdp import Wallet
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions import CdpAction
from cdp_agentkit_core.actions.boost.constants import (
    BOOST_CORE_ABI,
    DEPLOYS,
    get_boost_core_address
)

BOOST_CREATE_PROMPT = """
This tool will create a new Boost using a deployed Boost Core contract. This tool takes . It uses a bonding curve so there is no need to add liquidity to the pool upfront. It is only supported on Base Sepolia and Base Mainnet.
"""


class BoostCreateBoostInput(BaseModel):
    """Input argument schema for create Boost action."""

    name: str = Field(
        ...,
        description="The name of the token to create, e.g. WowCoin",
    )
    symbol: str = Field(
        ...,
        description="The symbol of the token to create, e.g. WOW",
    )


def boost_create_boost(wallet: Wallet, name: str, symbol: str) -> str:
    """Create a Zora Wow ERC20 memecoin.

    Args:
        wallet (Wallet): The wallet to create the token from.
        name (str): The name of the token to create.
        symbol (str): The symbol of the token to create.

    Returns:
        str: A message containing the token creation details.

    """
    core_address = get_boost_core_address(wallet.network_id)

    invocation = wallet.invoke_contract(
        contract_address=core_address,
        method="createBoost",
        abi=BOOST_CORE_ABI,
        args={
            "data_": "0x0000000000000000000000000000000000000000",
        },
    ).wait()

    return f"Created WoW ERC20 memecoin {name} with symbol {symbol} on network {wallet.network_id}.\nTransaction hash for the token creation: {invocation.transaction.transaction_hash}\nTransaction link for the token creation: {invocation.transaction.transaction_link}"


class BoostCreateBoostAction(CdpAction):
    """Boost create Boost action."""

    name: str = "boost_create_boost"
    description: str = BOOST_CREATE_PROMPT
    args_schema: type[BaseModel] | None = BoostCreateBoostInput
    func: Callable[..., str] = boost_create_boost
