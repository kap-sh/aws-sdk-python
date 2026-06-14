"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CoinbaseCdpTokenResponseOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type


class CoinbaseCdpTokenResponseOutput(TypedDict):
    bearer_token: "aws_sdk_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type.CoinbaseCdpPaymentJwtTokenType"
    """<p>Bearer Token for Authorization header.</p>"""
    wallet_auth_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.coinbase_cdp_payment_jwt_token_type.CoinbaseCdpPaymentJwtTokenType"
    ]
    """<p>Wallet Auth Token for X-Wallet-Auth header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoinbaseCdpTokenResponseOutput) -> dict:
    out: dict = {}
    out["bearerToken"] = value["bearer_token"]
    if "wallet_auth_token" in value:
        out["walletAuthToken"] = value["wallet_auth_token"]
    return out


def deserialize_json(data: dict) -> CoinbaseCdpTokenResponseOutput:
    out: CoinbaseCdpTokenResponseOutput = {}  # type: ignore[typeddict-item]
    if "bearerToken" in data:
        out["bearer_token"] = data["bearerToken"]
    else:
        raise DeserializationError(
            "CoinbaseCdpTokenResponseOutput.bearer_token required"
        )
    if "walletAuthToken" in data:
        out["wallet_auth_token"] = data["walletAuthToken"]
    return out
