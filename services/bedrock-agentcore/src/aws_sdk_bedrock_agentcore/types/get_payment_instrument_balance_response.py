"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentInstrumentBalanceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_instrument_id
    import aws_sdk_bedrock_agentcore.types.token_balance

class GetPaymentInstrumentBalanceResponse(TypedDict):
    payment_instrument_id: "aws_sdk_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId"
    """<p>The ID of the payment instrument.</p>"""
    token_balance: "aws_sdk_bedrock_agentcore.types.token_balance.TokenBalance"
    """<p>The balance of the supported token on the requested chain.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentInstrumentBalanceResponse) -> dict:
    out: dict = {}
    out["paymentInstrumentId"] = value["payment_instrument_id"]
    import aws_sdk_bedrock_agentcore.types.token_balance
    out["tokenBalance"] = aws_sdk_bedrock_agentcore.types.token_balance.serialize_json(value["token_balance"])
    return out


def deserialize_json(data: dict) -> GetPaymentInstrumentBalanceResponse:
    out: GetPaymentInstrumentBalanceResponse = {}  # type: ignore[typeddict-item]
    if "paymentInstrumentId" in data:
        out["payment_instrument_id"] = data["paymentInstrumentId"]
    else:
        raise DeserializationError("GetPaymentInstrumentBalanceResponse.payment_instrument_id required")
    if "tokenBalance" in data:
        import aws_sdk_bedrock_agentcore.types.token_balance
        out["token_balance"] = aws_sdk_bedrock_agentcore.types.token_balance.deserialize_json(data["tokenBalance"])
    else:
        raise DeserializationError("GetPaymentInstrumentBalanceResponse.token_balance required")
    return out