"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreatePaymentInstrumentResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_instrument

class CreatePaymentInstrumentResponse(TypedDict):
    payment_instrument: "aws_sdk_bedrock_agentcore.types.payment_instrument.PaymentInstrument"
    """<p>The created payment instrument.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentInstrumentResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_instrument
    out["paymentInstrument"] = aws_sdk_bedrock_agentcore.types.payment_instrument.serialize_json(value["payment_instrument"])
    return out


def deserialize_json(data: dict) -> CreatePaymentInstrumentResponse:
    out: CreatePaymentInstrumentResponse = {}  # type: ignore[typeddict-item]
    if "paymentInstrument" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument
        out["payment_instrument"] = aws_sdk_bedrock_agentcore.types.payment_instrument.deserialize_json(data["paymentInstrument"])
    else:
        raise DeserializationError("CreatePaymentInstrumentResponse.payment_instrument required")
    return out