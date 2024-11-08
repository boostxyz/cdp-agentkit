BOOST_REGISTRY_ABI = [
  {
    "inputs": [
      {
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "registryType",
        "type": "uint8"
      },
      {
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      }
    ],
    "name": "AlreadyRegistered",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "NotACloneable",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      }
    ],
    "name": "NotRegistered",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "Reentrancy",
    "type": "error"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "registryType",
        "type": "uint8"
      },
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "baseImplementation",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "contract ACloneable",
        "name": "deployedInstance",
        "type": "address"
      }
    ],
    "name": "Deployed",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "registryType",
        "type": "uint8"
      },
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "implementation",
        "type": "address"
      }
    ],
    "name": "Registered",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "type_",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "base_",
        "type": "address"
      },
      {
        "internalType": "string",
        "name": "name_",
        "type": "string"
      },
      {
        "internalType": "bytes",
        "name": "data_",
        "type": "bytes"
      }
    ],
    "name": "deployClone",
    "outputs": [
      {
        "internalType": "contract ACloneable",
        "name": "instance",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "identifier_",
        "type": "bytes32"
      }
    ],
    "name": "getBaseImplementation",
    "outputs": [
      {
        "internalType": "contract ACloneable",
        "name": "implementation",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "identifier_",
        "type": "bytes32"
      }
    ],
    "name": "getClone",
    "outputs": [
      {
        "components": [
          {
            "internalType": "enum ABoostRegistry.RegistryType",
            "name": "baseType",
            "type": "uint8"
          },
          {
            "internalType": "contract ACloneable",
            "name": "instance",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "deployer",
            "type": "address"
          },
          {
            "internalType": "string",
            "name": "name",
            "type": "string"
          }
        ],
        "internalType": "struct ABoostRegistry.Clone",
        "name": "clone",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "type_",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "base_",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "deployer_",
        "type": "address"
      },
      {
        "internalType": "string",
        "name": "name_",
        "type": "string"
      }
    ],
    "name": "getCloneIdentifier",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "deployer_",
        "type": "address"
      }
    ],
    "name": "getClones",
    "outputs": [
      {
        "internalType": "bytes32[]",
        "name": "",
        "type": "bytes32[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "type_",
        "type": "uint8"
      },
      {
        "internalType": "string",
        "name": "name_",
        "type": "string"
      }
    ],
    "name": "getIdentifier",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "identifier",
        "type": "bytes32"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "enum ABoostRegistry.RegistryType",
        "name": "type_",
        "type": "uint8"
      },
      {
        "internalType": "string",
        "name": "name_",
        "type": "string"
      },
      {
        "internalType": "address",
        "name": "implementation_",
        "type": "address"
      }
    ],
    "name": "register",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "interfaceId",
        "type": "bytes4"
      }
    ],
    "name": "supportsInterface",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
]

BOOST_CORE_ABI = [
  {
    "inputs": [
      {
        "internalType": "contract BoostRegistry",
        "name": "registry_",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "protocolFeeReceiver_",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "AlreadyInitialized",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "caller",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "ClaimFailed",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "caller",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "ClawbackFailed",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "InvalidInitialization",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "bytes4",
        "name": "expectedInterface",
        "type": "bytes4"
      },
      {
        "internalType": "address",
        "name": "instance",
        "type": "address"
      }
    ],
    "name": "InvalidInstance",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NewOwnerIsZeroAddress",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NoHandoverRequest",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "NotImplemented",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "Reentrancy",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "Unauthorized",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "Unauthorized",
    "type": "error"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "boostId",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "incentiveId",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "claimant",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "referrer",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "bytes",
        "name": "data",
        "type": "bytes"
      }
    ],
    "name": "BoostClaimed",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "boostId",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "action",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "incentiveCount",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "validator",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "allowList",
        "type": "address"
      },
      {
        "indexed": False,
        "internalType": "address",
        "name": "budget",
        "type": "address"
      }
    ],
    "name": "BoostCreated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "pendingOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipHandoverCanceled",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "pendingOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipHandoverRequested",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "oldOwner",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "OwnershipTransferred",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "boostId",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "incentiveId",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      },
      {
        "indexed": True,
        "internalType": "address",
        "name": "recipient",
        "type": "address"
      }
    ],
    "name": "ProtocolFeesCollected",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "FEE_DENOMINATOR",
    "outputs": [
      {
        "internalType": "uint64",
        "name": "",
        "type": "uint64"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "cancelOwnershipHandover",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "boostId_",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "incentiveId_",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "referrer_",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data_",
        "type": "bytes"
      }
    ],
    "name": "claimIncentive",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "boostId_",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "incentiveId_",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "referrer_",
        "type": "address"
      },
      {
        "internalType": "bytes",
        "name": "data_",
        "type": "bytes"
      },
      {
        "internalType": "address",
        "name": "claimant",
        "type": "address"
      }
    ],
    "name": "claimIncentiveFor",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes",
        "name": "data_",
        "type": "bytes"
      },
      {
        "internalType": "uint256",
        "name": "boostId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "incentiveId",
        "type": "uint256"
      }
    ],
    "name": "clawback",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      },
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "pendingOwner",
        "type": "address"
      }
    ],
    "name": "completeOwnershipHandover",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes",
        "name": "data_",
        "type": "bytes"
      }
    ],
    "name": "createBoost",
    "outputs": [
      {
        "components": [
          {
            "internalType": "contract AAction",
            "name": "action",
            "type": "address"
          },
          {
            "internalType": "contract AValidator",
            "name": "validator",
            "type": "address"
          },
          {
            "internalType": "contract AAllowList",
            "name": "allowList",
            "type": "address"
          },
          {
            "internalType": "contract ABudget",
            "name": "budget",
            "type": "address"
          },
          {
            "internalType": "contract AIncentive[]",
            "name": "incentives",
            "type": "address[]"
          },
          {
            "internalType": "uint64",
            "name": "protocolFee",
            "type": "uint64"
          },
          {
            "internalType": "uint256",
            "name": "maxParticipants",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "owner",
            "type": "address"
          }
        ],
        "internalType": "struct BoostLib.Boost",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "createBoostAuth",
    "outputs": [
      {
        "internalType": "contract IAuth",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "index",
        "type": "uint256"
      }
    ],
    "name": "getBoost",
    "outputs": [
      {
        "components": [
          {
            "internalType": "contract AAction",
            "name": "action",
            "type": "address"
          },
          {
            "internalType": "contract AValidator",
            "name": "validator",
            "type": "address"
          },
          {
            "internalType": "contract AAllowList",
            "name": "allowList",
            "type": "address"
          },
          {
            "internalType": "contract ABudget",
            "name": "budget",
            "type": "address"
          },
          {
            "internalType": "contract AIncentive[]",
            "name": "incentives",
            "type": "address[]"
          },
          {
            "internalType": "uint64",
            "name": "protocolFee",
            "type": "uint64"
          },
          {
            "internalType": "uint256",
            "name": "maxParticipants",
            "type": "uint256"
          },
          {
            "internalType": "address",
            "name": "owner",
            "type": "address"
          }
        ],
        "internalType": "struct BoostLib.Boost",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "getBoostCount",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "key",
        "type": "bytes32"
      }
    ],
    "name": "getIncentiveFeesInfo",
    "outputs": [
      {
        "components": [
          {
            "internalType": "enum ABudget.AssetType",
            "name": "assetType",
            "type": "uint8"
          },
          {
            "internalType": "address",
            "name": "asset",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "protocolFeesRemaining",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "protocolFee",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "tokenId",
            "type": "uint256"
          }
        ],
        "internalType": "struct BoostCore.IncentiveDisbursalInfo",
        "name": "",
        "type": "tuple"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "",
        "type": "bytes32"
      }
    ],
    "name": "incentivesFeeInfo",
    "outputs": [
      {
        "internalType": "enum ABudget.AssetType",
        "name": "assetType",
        "type": "uint8"
      },
      {
        "internalType": "address",
        "name": "asset",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "protocolFeesRemaining",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "protocolFee",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "owner",
    "outputs": [
      {
        "internalType": "address",
        "name": "result",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "pendingOwner",
        "type": "address"
      }
    ],
    "name": "ownershipHandoverExpiresAt",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "result",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "protocolFee",
    "outputs": [
      {
        "internalType": "uint64",
        "name": "",
        "type": "uint64"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "protocolFeeReceiver",
    "outputs": [
      {
        "internalType": "address",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "registry",
    "outputs": [
      {
        "internalType": "contract BoostRegistry",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "renounceOwnership",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "requestOwnershipHandover",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "auth_",
        "type": "address"
      }
    ],
    "name": "setCreateBoostAuth",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint64",
        "name": "protocolFee_",
        "type": "uint64"
      }
    ],
    "name": "setProtocolFee",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "protocolFeeReceiver_",
        "type": "address"
      }
    ],
    "name": "setProtocolFeeReceiver",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "boostId",
        "type": "uint256"
      },
      {
        "internalType": "uint256",
        "name": "incentiveId",
        "type": "uint256"
      }
    ],
    "name": "settleProtocolFees",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "newOwner",
        "type": "address"
      }
    ],
    "name": "transferOwnership",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  }
]

DEPLOYS = {
 "base-mainnet": {
   "AllowListIncentive": "0x5AA51DCC8F3bdeD3a270613d3C9682EA10062782",
   "BoostCore": "0xE2D376c791cAA498b86ebfc3C87121112Fd8Cd5b",
   "BoostRegistry": "0x694c04324C2F4D97eBF98FaC633DF54E7A95334f",
   "CGDAIncentive": "0x2B5E78665C7e79791078dfFE94f04c1d1C42558F",
   "ERC20Incentive": "0x449094B4fb2A9Bf25dd9876E90ab2310aa386697",
   "ERC20VariableCriteriaIncentive": "0x96b23C5B81FEA6Da7f12B70050D4C4f76d3a9D0D",
   "ERC20VariableIncentive": "0x8Db3E5226FD46F14E666954F65557539e7025136",
   "EventAction": "0x674f6b02e0B1159D61DFFCEe096776fd3B2bb7C1",
   "ManagedBudget": "0xC9fB769A6A1e71663E85AE30CCfE97bf67B6d42F",
   "OpenAllowList": "0xa62b2c812F7838e3032917f76B7A33333801559E",
   "PointsIncentive": "0x817aD27DF5a20a995bCD87962A8B32eB60c6c2D9",
   "SignerValidator": "0x72D733558473Cb3e9A66B25B99cb9810111f5E11",
   "SimpleAllowList": "0x5aE607016b0a742D0eF3aDD7B3257881bA383CB3",
   "SimpleDenyList": "0x5b0eD712b54775584cbB28fe7954e854781AA805"
 },
 "arbitrum-mainnet": {
   "AllowListIncentive": "0x5AA51DCC8F3bdeD3a270613d3C9682EA10062782",
   "BoostCore": "0xE2D376c791cAA498b86ebfc3C87121112Fd8Cd5b",
   "BoostRegistry": "0x694c04324C2F4D97eBF98FaC633DF54E7A95334f",
   "CGDAIncentive": "0x2B5E78665C7e79791078dfFE94f04c1d1C42558F",
   "ERC20Incentive": "0x449094B4fb2A9Bf25dd9876E90ab2310aa386697",
   "ERC20VariableCriteriaIncentive": "0x96b23C5B81FEA6Da7f12B70050D4C4f76d3a9D0D",
   "ERC20VariableIncentive": "0x8Db3E5226FD46F14E666954F65557539e7025136",
   "EventAction": "0x674f6b02e0B1159D61DFFCEe096776fd3B2bb7C1",
   "ManagedBudget": "0xC9fB769A6A1e71663E85AE30CCfE97bf67B6d42F",
   "OpenAllowList": "0xa62b2c812F7838e3032917f76B7A33333801559E",
   "PointsIncentive": "0x817aD27DF5a20a995bCD87962A8B32eB60c6c2D9",
   "SignerValidator": "0x72D733558473Cb3e9A66B25B99cb9810111f5E11",
   "SimpleAllowList": "0x5aE607016b0a742D0eF3aDD7B3257881bA383CB3",
   "SimpleDenyList": "0x5b0eD712b54775584cbB28fe7954e854781AA805"
 },
 "base-sepolia": {
   "AllowListIncentive": "0x5AA51DCC8F3bdeD3a270613d3C9682EA10062782",
   "BoostCore": "0xE2D376c791cAA498b86ebfc3C87121112Fd8Cd5b",
   "BoostRegistry": "0x694c04324C2F4D97eBF98FaC633DF54E7A95334f",
   "CGDAIncentive": "0x2B5E78665C7e79791078dfFE94f04c1d1C42558F",
   "ERC20Incentive": "0x449094B4fb2A9Bf25dd9876E90ab2310aa386697",
   "ERC20VariableCriteriaIncentive": "0x96b23C5B81FEA6Da7f12B70050D4C4f76d3a9D0D",
   "ERC20VariableIncentive": "0x8Db3E5226FD46F14E666954F65557539e7025136",
   "EventAction": "0x674f6b02e0B1159D61DFFCEe096776fd3B2bb7C1",
   "ManagedBudget": "0xC9fB769A6A1e71663E85AE30CCfE97bf67B6d42F",
   "OpenAllowList": "0xa62b2c812F7838e3032917f76B7A33333801559E",
   "PointsIncentive": "0x817aD27DF5a20a995bCD87962A8B32eB60c6c2D9",
   "SignerValidator": "0x72D733558473Cb3e9A66B25B99cb9810111f5E11",
   "SimpleAllowList": "0x5aE607016b0a742D0eF3aDD7B3257881bA383CB3",
   "SimpleDenyList": "0x5b0eD712b54775584cbB28fe7954e854781AA805"
 }
}


def get_boost_registry_address(network: str) -> str:
    """Get the Boost Registry contract address for the specified network.

    Args:
        network (str): The network to get the contract address for.
            Valid networks are: base-mainnet, base-sepolia, and arbitrum-mainnet.

    Returns:
        str: The contract address for Boost Registry on the specified network.

    Raises:
        ValueError: If the specified network is not supported.

    """
    if network not in DEPLOYS:
        raise ValueError(
            f"Invalid network: {network}. Valid networks are: {', '.join(DEPLOYS.keys())}"
        )
    return DEPLOYS[network]["BoostRegistry"]

def get_boost_core_address(network: str) -> str:
    """Get the Boost Core contract address for the specified network.

    Args:
        network (str): The network ID to get the contract address for.
            Valid networks are: base-mainnet, base-sepolia, and arbitrum-mainnet.

    Returns:
        str: The contract address for Boost Core on the specified network.

    Raises:
        ValueError: If the specified network is not supported.

    """
    if network not in DEPLOYS:
        raise ValueError(
            f"Invalid network: {network}. Valid networks are: {', '.join(DEPLOYS.keys())}"
        )
    return DEPLOYS[network]["BoostCore"]
