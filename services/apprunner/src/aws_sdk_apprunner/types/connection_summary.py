"""Generated from Smithy shape ``com.amazonaws.apprunner#ConnectionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.connection_name
    import aws_sdk_apprunner.types.connection_status
    import aws_sdk_apprunner.types.provider_type
    import aws_sdk_apprunner.types.timestamp


class ConnectionSummary(TypedDict):
    connection_name: NotRequired[
        "aws_sdk_apprunner.types.connection_name.ConnectionName"
    ]
    """<p>The customer-provided connection name.</p>"""
    connection_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this connection.</p>"""
    provider_type: NotRequired["aws_sdk_apprunner.types.provider_type.ProviderType"]
    """<p>The source repository provider.</p>"""
    status: NotRequired["aws_sdk_apprunner.types.connection_status.ConnectionStatus"]
    """<p>The current state of the App Runner connection. When the state is <code>AVAILABLE</code>, you can use the connection to create an App Runner service.</p>"""
    created_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The App Runner connection creation time, expressed as a Unix time stamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionSummary) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "provider_type" in value:
        import aws_sdk_apprunner.types.provider_type

        out["ProviderType"] = (
            aws_sdk_apprunner.types.provider_type.serialize_aws_json_1_0(
                value["provider_type"]
            )
        )
    if "status" in value:
        import aws_sdk_apprunner.types.connection_status

        out["Status"] = (
            aws_sdk_apprunner.types.connection_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "created_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["CreatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionSummary:
    out: ConnectionSummary = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "ProviderType" in data:
        import aws_sdk_apprunner.types.provider_type

        out["provider_type"] = (
            aws_sdk_apprunner.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if "Status" in data:
        import aws_sdk_apprunner.types.connection_status

        out["status"] = (
            aws_sdk_apprunner.types.connection_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "CreatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["created_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    return out
