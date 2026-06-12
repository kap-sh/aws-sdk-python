"""Generated from Smithy shape ``com.amazonaws.appflow#CreateConnectorProfileRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.client_token
    import aws_sdk_appflow.types.connection_mode
    import aws_sdk_appflow.types.connector_label
    import aws_sdk_appflow.types.connector_profile_config
    import aws_sdk_appflow.types.connector_profile_name
    import aws_sdk_appflow.types.connector_type
    import aws_sdk_appflow.types.kms_arn


class CreateConnectorProfileRequest(TypedDict):
    connector_profile_name: (
        "aws_sdk_appflow.types.connector_profile_name.ConnectorProfileName"
    )
    """<p> The name of the connector profile. The name is unique for each <code>ConnectorProfile</code> in your Amazon Web Services account. </p>"""
    kms_arn: NotRequired["aws_sdk_appflow.types.kms_arn.KMSArn"]
    """<p> The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key. </p>"""
    connector_type: "aws_sdk_appflow.types.connector_type.ConnectorType"
    """<p> The type of connector, such as Salesforce, Amplitude, and so on. </p>"""
    connector_label: NotRequired["aws_sdk_appflow.types.connector_label.ConnectorLabel"]
    """<p>The label of the connector. The label is unique for each <code>ConnectorRegistration</code> in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.</p>"""
    connection_mode: "aws_sdk_appflow.types.connection_mode.ConnectionMode"
    """<p> Indicates the connection mode and specifies whether it is public or private. Private flows use Amazon Web Services PrivateLink to route data over Amazon Web Services infrastructure without exposing it to the public internet. </p>"""
    connector_profile_config: (
        "aws_sdk_appflow.types.connector_profile_config.ConnectorProfileConfig"
    )
    """<p> Defines the connector-specific configuration and credentials. </p>"""
    client_token: NotRequired["aws_sdk_appflow.types.client_token.ClientToken"]
    """<p>The <code>clientToken</code> parameter is an idempotency token. It ensures that your <code>CreateConnectorProfile</code> request completes only once. You choose the value to pass. For example, if you don't receive a response from your request, you can safely retry the request with the same <code>clientToken</code> parameter value.</p> <p>If you omit a <code>clientToken</code> value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.</p> <p>If you specify input parameters that differ from your first request, an error occurs. If you use a different value for <code>clientToken</code>, Amazon AppFlow considers it a new call to <code>CreateConnectorProfile</code>. The token is active for 8 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorProfileRequest) -> dict:
    out: dict = {}
    out["connectorProfileName"] = value["connector_profile_name"]
    if "kms_arn" in value:
        out["kmsArn"] = value["kms_arn"]
    import aws_sdk_appflow.types.connector_type

    out["connectorType"] = aws_sdk_appflow.types.connector_type.serialize_json(
        value["connector_type"]
    )
    if "connector_label" in value:
        out["connectorLabel"] = value["connector_label"]
    import aws_sdk_appflow.types.connection_mode

    out["connectionMode"] = aws_sdk_appflow.types.connection_mode.serialize_json(
        value["connection_mode"]
    )
    import aws_sdk_appflow.types.connector_profile_config

    out["connectorProfileConfig"] = (
        aws_sdk_appflow.types.connector_profile_config.serialize_json(
            value["connector_profile_config"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectorProfileRequest:
    out: CreateConnectorProfileRequest = {}  # type: ignore[typeddict-item]
    if "connectorProfileName" in data:
        out["connector_profile_name"] = data["connectorProfileName"]
    else:
        raise DeserializationError(
            "CreateConnectorProfileRequest.connector_profile_name required"
        )
    if "kmsArn" in data:
        out["kms_arn"] = data["kmsArn"]
    if "connectorType" in data:
        import aws_sdk_appflow.types.connector_type

        out["connector_type"] = aws_sdk_appflow.types.connector_type.deserialize_json(
            data["connectorType"]
        )
    else:
        raise DeserializationError(
            "CreateConnectorProfileRequest.connector_type required"
        )
    if "connectorLabel" in data:
        out["connector_label"] = data["connectorLabel"]
    if "connectionMode" in data:
        import aws_sdk_appflow.types.connection_mode

        out["connection_mode"] = aws_sdk_appflow.types.connection_mode.deserialize_json(
            data["connectionMode"]
        )
    else:
        raise DeserializationError(
            "CreateConnectorProfileRequest.connection_mode required"
        )
    if "connectorProfileConfig" in data:
        import aws_sdk_appflow.types.connector_profile_config

        out["connector_profile_config"] = (
            aws_sdk_appflow.types.connector_profile_config.deserialize_json(
                data["connectorProfileConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectorProfileRequest.connector_profile_config required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
