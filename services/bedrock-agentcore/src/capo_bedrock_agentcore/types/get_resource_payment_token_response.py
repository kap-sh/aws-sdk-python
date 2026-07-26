"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GetResourcePaymentTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.payment_token_response_output


class GetResourcePaymentTokenResponse(TypedDict, closed=True):
    payment_token_response: "capo_bedrock_agentcore.types.payment_token_response_output.PaymentTokenResponseOutput"
    """<p>Vendor-specific token response output. Contains all response data in a type-safe, vendor-specific structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcePaymentTokenResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.payment_token_response_output

    out["paymentTokenResponse"] = (
        capo_bedrock_agentcore.types.payment_token_response_output.serialize_json(
            value["payment_token_response"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetResourcePaymentTokenResponse:
    out: GetResourcePaymentTokenResponse = {}  # type: ignore[typeddict-item]
    if "paymentTokenResponse" in data:
        import capo_bedrock_agentcore.types.payment_token_response_output

        out["payment_token_response"] = (
            capo_bedrock_agentcore.types.payment_token_response_output.deserialize_json(
                data["paymentTokenResponse"]
            )
        )
    else:
        raise DeserializationError(
            "GetResourcePaymentTokenResponse.payment_token_response required"
        )
    return out
