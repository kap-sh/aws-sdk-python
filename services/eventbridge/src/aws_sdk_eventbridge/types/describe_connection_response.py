"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeConnectionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.connection_arn
    import aws_sdk_eventbridge.types.connection_auth_response_parameters
    import aws_sdk_eventbridge.types.connection_authorization_type
    import aws_sdk_eventbridge.types.connection_description
    import aws_sdk_eventbridge.types.connection_name
    import aws_sdk_eventbridge.types.connection_state
    import aws_sdk_eventbridge.types.connection_state_reason
    import aws_sdk_eventbridge.types.describe_connection_connectivity_parameters
    import aws_sdk_eventbridge.types.kms_key_identifier
    import aws_sdk_eventbridge.types.secrets_manager_secret_arn
    import aws_sdk_eventbridge.types.timestamp


class DescribeConnectionResponse(TypedDict):
    connection_arn: NotRequired[
        "aws_sdk_eventbridge.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection retrieved.</p>"""
    name: NotRequired["aws_sdk_eventbridge.types.connection_name.ConnectionName"]
    """<p>The name of the connection retrieved.</p>"""
    description: NotRequired[
        "aws_sdk_eventbridge.types.connection_description.ConnectionDescription"
    ]
    """<p>The description for the connection retrieved.</p>"""
    invocation_connectivity_parameters: NotRequired[
        "aws_sdk_eventbridge.types.describe_connection_connectivity_parameters.DescribeConnectionConnectivityParameters"
    ]
    """<p>For connections to private APIs The parameters EventBridge uses to invoke the resource endpoint.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/connection-private.html\">Connecting to private APIs</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""
    connection_state: NotRequired[
        "aws_sdk_eventbridge.types.connection_state.ConnectionState"
    ]
    """<p>The state of the connection retrieved.</p>"""
    state_reason: NotRequired[
        "aws_sdk_eventbridge.types.connection_state_reason.ConnectionStateReason"
    ]
    """<p>The reason that the connection is in the current connection state.</p>"""
    authorization_type: NotRequired[
        "aws_sdk_eventbridge.types.connection_authorization_type.ConnectionAuthorizationType"
    ]
    """<p>The type of authorization specified for the connection.</p>"""
    secret_arn: NotRequired[
        "aws_sdk_eventbridge.types.secrets_manager_secret_arn.SecretsManagerSecretArn"
    ]
    """<p>The ARN of the secret created from the authorization parameters specified for the connection.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_eventbridge.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The identifier of the KMS customer managed key for EventBridge to use to encrypt the connection, if one has been specified.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/encryption-connections.html\">Encrypting connections</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    auth_parameters: NotRequired[
        "aws_sdk_eventbridge.types.connection_auth_response_parameters.ConnectionAuthResponseParameters"
    ]
    """<p>The parameters to use for authorization for the connection.</p>"""
    creation_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was created.</p>"""
    last_modified_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last modified.</p>"""
    last_authorized_time: NotRequired["aws_sdk_eventbridge.types.timestamp.Timestamp"]
    """<p>A time stamp for the time that the connection was last authorized.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionResponse) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "invocation_connectivity_parameters" in value:
        import aws_sdk_eventbridge.types.describe_connection_connectivity_parameters

        out["InvocationConnectivityParameters"] = (
            aws_sdk_eventbridge.types.describe_connection_connectivity_parameters.serialize_aws_json_1_1(
                value["invocation_connectivity_parameters"]
            )
        )
    if "connection_state" in value:
        import aws_sdk_eventbridge.types.connection_state

        out["ConnectionState"] = (
            aws_sdk_eventbridge.types.connection_state.serialize_aws_json_1_1(
                value["connection_state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "authorization_type" in value:
        import aws_sdk_eventbridge.types.connection_authorization_type

        out["AuthorizationType"] = (
            aws_sdk_eventbridge.types.connection_authorization_type.serialize_aws_json_1_1(
                value["authorization_type"]
            )
        )
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "auth_parameters" in value:
        import aws_sdk_eventbridge.types.connection_auth_response_parameters

        out["AuthParameters"] = (
            aws_sdk_eventbridge.types.connection_auth_response_parameters.serialize_aws_json_1_1(
                value["auth_parameters"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["CreationTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "last_authorized_time" in value:
        import aws_sdk_eventbridge.types.timestamp

        out["LastAuthorizedTime"] = (
            aws_sdk_eventbridge.types.timestamp.serialize_aws_json_1_1(
                value["last_authorized_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionResponse:
    out: DescribeConnectionResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "InvocationConnectivityParameters" in data:
        import aws_sdk_eventbridge.types.describe_connection_connectivity_parameters

        out["invocation_connectivity_parameters"] = (
            aws_sdk_eventbridge.types.describe_connection_connectivity_parameters.deserialize_aws_json_1_1(
                data["InvocationConnectivityParameters"]
            )
        )
    if "ConnectionState" in data:
        import aws_sdk_eventbridge.types.connection_state

        out["connection_state"] = (
            aws_sdk_eventbridge.types.connection_state.deserialize_aws_json_1_1(
                data["ConnectionState"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "AuthorizationType" in data:
        import aws_sdk_eventbridge.types.connection_authorization_type

        out["authorization_type"] = (
            aws_sdk_eventbridge.types.connection_authorization_type.deserialize_aws_json_1_1(
                data["AuthorizationType"]
            )
        )
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "AuthParameters" in data:
        import aws_sdk_eventbridge.types.connection_auth_response_parameters

        out["auth_parameters"] = (
            aws_sdk_eventbridge.types.connection_auth_response_parameters.deserialize_aws_json_1_1(
                data["AuthParameters"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["creation_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "LastAuthorizedTime" in data:
        import aws_sdk_eventbridge.types.timestamp

        out["last_authorized_time"] = (
            aws_sdk_eventbridge.types.timestamp.deserialize_aws_json_1_1(
                data["LastAuthorizedTime"]
            )
        )
    return out
