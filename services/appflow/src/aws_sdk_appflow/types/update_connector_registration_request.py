"""Generated from Smithy shape ``com.amazonaws.appflow#UpdateConnectorRegistrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.client_token
    import aws_sdk_appflow.types.connector_label
    import aws_sdk_appflow.types.connector_provisioning_config
    import aws_sdk_appflow.types.description


class UpdateConnectorRegistrationRequest(TypedDict):
    connector_label: "aws_sdk_appflow.types.connector_label.ConnectorLabel"
    """<p>The name of the connector. The name is unique for each connector registration in your AWS account.</p>"""
    description: NotRequired["aws_sdk_appflow.types.description.Description"]
    """<p>A description about the update that you're applying to the connector.</p>"""
    connector_provisioning_config: NotRequired[
        "aws_sdk_appflow.types.connector_provisioning_config.ConnectorProvisioningConfig"
    ]
    client_token: NotRequired["aws_sdk_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>UpdateConnectorRegistration</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>UpdateConnectorRegistration</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConnectorRegistrationRequest) -> dict:
    out: dict = {}
    out["connectorLabel"] = value["connector_label"]
    if "description" in value:
        out["description"] = value["description"]
    if "connector_provisioning_config" in value:
        import aws_sdk_appflow.types.connector_provisioning_config

        out["connectorProvisioningConfig"] = (
            aws_sdk_appflow.types.connector_provisioning_config.serialize_json(
                value["connector_provisioning_config"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateConnectorRegistrationRequest:
    out: UpdateConnectorRegistrationRequest = {}  # type: ignore[typeddict-item]
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    else:
        raise DeserializationError(
            "UpdateConnectorRegistrationRequest.connector_label required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "connectorProvisioningConfig" in data:
        import aws_sdk_appflow.types.connector_provisioning_config

        out["connector_provisioning_config"] = (
            aws_sdk_appflow.types.connector_provisioning_config.deserialize_json(
                data["connectorProvisioningConfig"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
