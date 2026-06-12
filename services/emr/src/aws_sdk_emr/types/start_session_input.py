"""Generated from Smithy shape ``com.amazonaws.emr#StartSessionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.client_request_token
    import aws_sdk_emr.types.cluster_id
    import aws_sdk_emr.types.configuration_list
    import aws_sdk_emr.types.iam_role_arn
    import aws_sdk_emr.types.long
    import aws_sdk_emr.types.session_monitoring_configuration
    import aws_sdk_emr.types.tag_list
    import aws_sdk_emr.types.xml_string_max_len256


class StartSessionInput(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>An optional name for the session.</p>"""
    cluster_id: NotRequired["aws_sdk_emr.types.cluster_id.ClusterId"]
    """<p>The ID of the cluster on which to start the session.</p>"""
    execution_role_arn: NotRequired["aws_sdk_emr.types.iam_role_arn.IAMRoleArn"]
    """<p>The execution role ARN for the session. Amazon EMR uses this role to access Amazon Web Services resources on your behalf during session execution.</p>"""
    engine_configurations: NotRequired[
        "aws_sdk_emr.types.configuration_list.ConfigurationList"
    ]
    """<p>The configuration overrides for the session. Only runtime configuration overrides are supported.</p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr.types.session_monitoring_configuration.SessionMonitoringConfiguration"
    ]
    """<p>The monitoring configuration that controls where session logs are published, such as Amazon S3, CloudWatch, or managed logging.</p>"""
    session_idle_timeout_in_minutes: NotRequired["aws_sdk_emr.types.long.Long"]
    """<p>The idle timeout, in minutes. If the session is idle for this duration, Amazon EMR EC2 automatically terminates it.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_emr.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client request token, the service returns the original response without performing the operation again.</p>"""
    tags: NotRequired["aws_sdk_emr.types.tag_list.TagList"]
    """<p>The tags to assign to the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartSessionInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "engine_configurations" in value:
        import aws_sdk_emr.types.configuration_list

        out["EngineConfigurations"] = (
            aws_sdk_emr.types.configuration_list.serialize_aws_json_1_1(
                value["engine_configurations"]
            )
        )
    if "monitoring_configuration" in value:
        import aws_sdk_emr.types.session_monitoring_configuration

        out["MonitoringConfiguration"] = (
            aws_sdk_emr.types.session_monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "session_idle_timeout_in_minutes" in value:
        out["SessionIdleTimeoutInMinutes"] = value["session_idle_timeout_in_minutes"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_emr.types.tag_list

        out["Tags"] = aws_sdk_emr.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> StartSessionInput:
    out: StartSessionInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "EngineConfigurations" in data:
        import aws_sdk_emr.types.configuration_list

        out["engine_configurations"] = (
            aws_sdk_emr.types.configuration_list.deserialize_aws_json_1_1(
                data["EngineConfigurations"]
            )
        )
    if "MonitoringConfiguration" in data:
        import aws_sdk_emr.types.session_monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_emr.types.session_monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if "SessionIdleTimeoutInMinutes" in data:
        out["session_idle_timeout_in_minutes"] = data["SessionIdleTimeoutInMinutes"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_emr.types.tag_list

        out["tags"] = aws_sdk_emr.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
