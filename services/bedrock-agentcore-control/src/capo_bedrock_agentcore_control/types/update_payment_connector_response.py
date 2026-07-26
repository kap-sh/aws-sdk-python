"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePaymentConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_status
    import capo_bedrock_agentcore_control.types.payment_connector_type
    import capo_bedrock_agentcore_control.types.payment_manager_id


class UpdatePaymentConnectorResponse(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the updated payment connector.</p>"""
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the updated payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the updated payment connector.</p>"""
    credential_provider_configurations: "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    """<p>The credential provider configurations for the updated payment connector.</p>"""
    last_updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the updated payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePaymentConnectorResponse) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["paymentManagerId"] = value["payment_manager_id"]
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        capo_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations

    out["credentialProviderConfigurations"] = (
        capo_bedrock_agentcore_control.types.credentials_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePaymentConnectorResponse:
    out: UpdatePaymentConnectorResponse = {}  # type: ignore[typeddict-item]
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "UpdatePaymentConnectorResponse.payment_connector_id required"
        )
    if "paymentManagerId" in data:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "UpdatePaymentConnectorResponse.payment_manager_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdatePaymentConnectorResponse.name required")
    if "type" in data:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("UpdatePaymentConnectorResponse.type required")
    if "credentialProviderConfigurations" in data:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePaymentConnectorResponse.credential_provider_configurations required"
        )
    if "lastUpdatedAt" in data:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePaymentConnectorResponse.last_updated_at required"
        )
    if "status" in data:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdatePaymentConnectorResponse.status required")
    return out
