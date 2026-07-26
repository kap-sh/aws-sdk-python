"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_manager_id


class GetPaymentConnectorRequest(TypedDict, closed=True):
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentConnectorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPaymentConnectorRequest:
    out: GetPaymentConnectorRequest = {}  # type: ignore[typeddict-item]
    return out
