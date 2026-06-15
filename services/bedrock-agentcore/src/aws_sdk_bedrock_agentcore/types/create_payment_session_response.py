"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreatePaymentSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.payment_session


class CreatePaymentSessionResponse(TypedDict):
    payment_session: "aws_sdk_bedrock_agentcore.types.payment_session.PaymentSession"
    """<p>The created payment session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentSessionResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.payment_session

    out["paymentSession"] = (
        aws_sdk_bedrock_agentcore.types.payment_session.serialize_json(
            value["payment_session"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePaymentSessionResponse:
    out: CreatePaymentSessionResponse = {}  # type: ignore[typeddict-item]
    if "paymentSession" in data:
        import aws_sdk_bedrock_agentcore.types.payment_session

        out["payment_session"] = (
            aws_sdk_bedrock_agentcore.types.payment_session.deserialize_json(
                data["paymentSession"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentSessionResponse.payment_session required"
        )
    return out
