"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PaymentConnectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_status
    import capo_bedrock_agentcore_control.types.payment_connector_type


class PaymentConnectorSummary(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the payment connector.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the payment connector, which determines the payment provider integration.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentConnectorSummary) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> PaymentConnectorSummary:
    out: PaymentConnectorSummary = {}  # type: ignore[typeddict-item]
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "PaymentConnectorSummary.payment_connector_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("PaymentConnectorSummary.name required")
    if "type" in data:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("PaymentConnectorSummary.type required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("PaymentConnectorSummary.status required")
    if "lastUpdatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError("PaymentConnectorSummary.last_updated_at required")
    return out
