"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetPaymentConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_id
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_name
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_status
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_type
    import aws_sdk_bedrock_agentcore_control.types.payments_description


class GetPaymentConnectorResponse(TypedDict, closed=True):
    payment_connector_id: "aws_sdk_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId"
    """<p>The unique identifier of the payment connector.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName"
    """<p>The name of the payment connector.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>The description of the payment connector.</p>"""
    type: "aws_sdk_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
    """<p>The type of the payment connector, which determines the payment provider integration.</p>"""
    credential_provider_configurations: "aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
    """<p>The credential provider configurations for the payment connector.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the payment connector was created.</p>"""
    last_updated_at: (
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp when the payment connector was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.payment_connector_status.PaymentConnectorStatus"
    """<p>The current status of the payment connector. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>DELETING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, and <code>DELETE_FAILED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPaymentConnectorResponse) -> dict:
    out: dict = {}
    out["paymentConnectorId"] = value["payment_connector_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_type

    out["type"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_connector_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations

    out["credentialProviderConfigurations"] = (
        aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations.serialize_json(
            value["credential_provider_configurations"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.payment_connector_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.payment_connector_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPaymentConnectorResponse:
    out: GetPaymentConnectorResponse = {}  # type: ignore[typeddict-item]
    if "paymentConnectorId" in data:
        out["payment_connector_id"] = data["paymentConnectorId"]
    else:
        raise DeserializationError(
            "GetPaymentConnectorResponse.payment_connector_id required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetPaymentConnectorResponse.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "type" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_connector_type

        out["type"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_connector_type.deserialize_json(
                data["type"]
            )
        )
    else:
        raise DeserializationError("GetPaymentConnectorResponse.type required")
    if "credentialProviderConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations

        out["credential_provider_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.credentials_provider_configurations.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "GetPaymentConnectorResponse.credential_provider_configurations required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("GetPaymentConnectorResponse.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetPaymentConnectorResponse.last_updated_at required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.payment_connector_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.payment_connector_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetPaymentConnectorResponse.status required")
    return out
