"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TokenBalance``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.blockchain_chain_id
    import aws_sdk_bedrock_agentcore.types.crypto_wallet_network
    import aws_sdk_bedrock_agentcore.types.instrument_balance_token


class TokenBalance(TypedDict, closed=True):
    amount: "str"
    """<p>Raw balance in the smallest denomination (e.g., USDC base units where 1 USDC = 1000000).</p>"""
    decimals: "int"
    """<p>Number of decimal places for the token (e.g., 6 for USDC).</p>"""
    token: "aws_sdk_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken"
    """<p>The supported token for this balance.</p>"""
    network: "aws_sdk_bedrock_agentcore.types.crypto_wallet_network.CryptoWalletNetwork"
    """<p>The blockchain network family (ETHEREUM or SOLANA).</p>"""
    chain: "aws_sdk_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId"
    """<p>The specific blockchain chain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TokenBalance) -> dict:
    out: dict = {}
    out["amount"] = value["amount"]
    out["decimals"] = value["decimals"]
    import aws_sdk_bedrock_agentcore.types.instrument_balance_token

    out["token"] = (
        aws_sdk_bedrock_agentcore.types.instrument_balance_token.serialize_json(
            value["token"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.crypto_wallet_network

    out["network"] = (
        aws_sdk_bedrock_agentcore.types.crypto_wallet_network.serialize_json(
            value["network"]
        )
    )
    import aws_sdk_bedrock_agentcore.types.blockchain_chain_id

    out["chain"] = aws_sdk_bedrock_agentcore.types.blockchain_chain_id.serialize_json(
        value["chain"]
    )
    return out


def deserialize_json(data: dict) -> TokenBalance:
    out: TokenBalance = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        raise DeserializationError("TokenBalance.amount required")
    if "decimals" in data:
        out["decimals"] = data["decimals"]
    else:
        raise DeserializationError("TokenBalance.decimals required")
    if "token" in data:
        import aws_sdk_bedrock_agentcore.types.instrument_balance_token

        out["token"] = (
            aws_sdk_bedrock_agentcore.types.instrument_balance_token.deserialize_json(
                data["token"]
            )
        )
    else:
        raise DeserializationError("TokenBalance.token required")
    if "network" in data:
        import aws_sdk_bedrock_agentcore.types.crypto_wallet_network

        out["network"] = (
            aws_sdk_bedrock_agentcore.types.crypto_wallet_network.deserialize_json(
                data["network"]
            )
        )
    else:
        raise DeserializationError("TokenBalance.network required")
    if "chain" in data:
        import aws_sdk_bedrock_agentcore.types.blockchain_chain_id

        out["chain"] = (
            aws_sdk_bedrock_agentcore.types.blockchain_chain_id.deserialize_json(
                data["chain"]
            )
        )
    else:
        raise DeserializationError("TokenBalance.chain required")
    return out
