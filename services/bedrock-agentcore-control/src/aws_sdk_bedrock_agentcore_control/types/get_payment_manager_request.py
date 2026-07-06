"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentManagerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.payment_manager_id


class GetPaymentManagerRequest(TypedDict, closed=True):
    payment_manager_id: (
        "aws_sdk_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the payment manager to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentManagerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPaymentManagerRequest:
    out: GetPaymentManagerRequest = {}  # type: ignore[typeddict-item]
    return out
