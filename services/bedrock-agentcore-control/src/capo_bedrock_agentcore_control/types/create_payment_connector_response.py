"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreatePaymentConnectorResponse``."""

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


class CreatePaymentConnectorResponse(TypedDict, closed=True):
    payment_connector_id: (
        "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    )
    """<p>The unique identifier of the created payment connector.</p>"""
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the parent payment manager.</p>"""
    name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the created payment connector.</p>"""
    type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the created payment connector.</p>"""
    credential_provider_configurations: "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    """<p>The credential provider configurations for the created payment connector.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was created.</p>"""
    status: "capo_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePaymentConnectorResponse) -> dict:
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

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePaymentConnectorResponse:
    out: CreatePaymentConnectorResponse = {}  # type: ignore[typeddict-item]
    if data.get("paymentConnectorId") is not None:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "CreatePaymentConnectorResponse.payment_connector_id required"
        )
    if data.get("paymentManagerId") is not None:
        out["payment_manager_id"] = data["paymentManagerId"]
    else:
        raise DeserializationError(
            "CreatePaymentConnectorResponse.payment_manager_id required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreatePaymentConnectorResponse.name required")
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentConnectorResponse.type required")
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePaymentConnectorResponse.credential_provider_configurations required"
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentConnectorResponse.created_at required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreatePaymentConnectorResponse.status required")
    return out
