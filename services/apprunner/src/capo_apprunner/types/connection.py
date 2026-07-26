"""Generated from Smithy shape ``com.amazonaws.apprunner#Connection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.app_runner_resource_arn
    import capo_apprunner.types.connection_name
    import capo_apprunner.types.connection_status
    import capo_apprunner.types.provider_type
    import capo_apprunner.types.timestamp


class Connection(TypedDict, closed=True):
    connection_name: NotRequired["capo_apprunner.types.connection_name.ConnectionName"]
    """<p>The customer-provided connection name.</p>"""
    connection_arn: NotRequired[
        "capo_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this connection.</p>"""
    provider_type: NotRequired["capo_apprunner.types.provider_type.ProviderType"]
    """<p>The source repository provider.</p>"""
    status: NotRequired["capo_apprunner.types.connection_status.ConnectionStatus"]
    """<p>The current state of the App Runner connection. When the state is <code>AVAILABLE</code>, you can use the connection to create an App Runner service.</p>"""
    created_at: NotRequired["capo_apprunner.types.timestamp.Timestamp"]
    """<p>The App Runner connection creation time, expressed as a Unix time stamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Connection) -> dict:
    out: dict = {}
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "provider_type" in value:
        import capo_apprunner.types.provider_type

        out["ProviderType"] = capo_apprunner.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    if "status" in value:
        import capo_apprunner.types.connection_status

        out["Status"] = capo_apprunner.types.connection_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "created_at" in value:
        import capo_apprunner.types.timestamp

        out["CreatedAt"] = capo_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Connection:
    out: Connection = {}  # type: ignore[typeddict-item]
    if "ConnectionName" in data:
        out["connection_name"] = data["ConnectionName"]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    if "ProviderType" in data:
        import capo_apprunner.types.provider_type

        out["provider_type"] = (
            capo_apprunner.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    if "Status" in data:
        import capo_apprunner.types.connection_status

        out["status"] = capo_apprunner.types.connection_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    if "CreatedAt" in data:
        import capo_apprunner.types.timestamp

        out["created_at"] = capo_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    return out
