"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeletePaymentSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_session_status


class DeletePaymentSessionResponse(TypedDict):
    status: (
        "aws_sdk_bedrock_agentcore.types.payment_session_status.PaymentSessionStatus"
    )
    """<p>The status of the deletion. Always DELETED for successful hard delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePaymentSessionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_session_status

    out["status"] = (
        aws_sdk_bedrock_agentcore.types.payment_session_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeletePaymentSessionResponse:
    out: DeletePaymentSessionResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_bedrock_agentcore.types.payment_session_status

        out["status"] = (
            aws_sdk_bedrock_agentcore.types.payment_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeletePaymentSessionResponse.status required")
    return out
