"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_session


class GetPaymentSessionResponse(TypedDict):
    payment_session: "aws_sdk_bedrock_agentcore.types.payment_session.PaymentSession"
    """<p>The payment session details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentSessionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_session

    out["paymentSession"] = (
        aws_sdk_bedrock_agentcore.types.payment_session.serialize_json(
            value["payment_session"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPaymentSessionResponse:
    out: GetPaymentSessionResponse = {}  # type: ignore[typeddict-item]
    if "paymentSession" in data:
        import aws_sdk_bedrock_agentcore.types.payment_session

        out["payment_session"] = (
            aws_sdk_bedrock_agentcore.types.payment_session.deserialize_json(
                data["paymentSession"]
            )
        )
    else:
        raise DeserializationError("GetPaymentSessionResponse.payment_session required")
    return out
