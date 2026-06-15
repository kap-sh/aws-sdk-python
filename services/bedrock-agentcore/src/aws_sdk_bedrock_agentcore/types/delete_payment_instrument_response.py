"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentInstrumentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_instrument_status


class DeletePaymentInstrumentResponse(TypedDict):
    status: "aws_sdk_bedrock_agentcore.types.payment_instrument_status.PaymentInstrumentStatus"
    """<p>The status of the instrument after deletion. Always DELETED for successful soft delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentInstrumentResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_instrument_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.payment_instrument_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeletePaymentInstrumentResponse:
    out: DeletePaymentInstrumentResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.payment_instrument_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.payment_instrument_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeletePaymentInstrumentResponse.status required")
    return out
