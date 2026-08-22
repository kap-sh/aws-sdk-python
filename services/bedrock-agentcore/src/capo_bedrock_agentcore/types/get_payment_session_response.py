"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetPaymentSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_session


class GetPaymentSessionResponse(TypedDict, closed=True):
    payment_session: "capo_bedrock_agentcore.types.payment_session.PaymentSession"
    """<p>The payment session details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentSessionResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_session

    out["paymentSession"] = capo_bedrock_agentcore.types.payment_session.serialize_json(
        value["payment_session"]
    )
    return out


def deserialize_json(data: dict) -> GetPaymentSessionResponse:
    out: GetPaymentSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentSession") is not None:
        import capo_bedrock_agentcore.types.payment_session

        out["payment_session"] = (
            capo_bedrock_agentcore.types.payment_session.deserialize_json(
                data["paymentSession"]
            )
        )
    else:
        raise DeserializationError("GetPaymentSessionResponse.payment_session required")
    return out
