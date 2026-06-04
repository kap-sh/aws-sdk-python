"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayServiceAwsLogsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class ExpressGatewayServiceAwsLogsConfiguration(TypedDict):
    log_group: "aws_sdk_ecs.types.string.String"
    """<p>The name of the CloudWatch Logs log group to send container logs to.</p>"""
    log_stream_prefix: "aws_sdk_ecs.types.string.String"
    """<p>The prefix for the CloudWatch Logs log stream names. The default for an Express service is <code>ecs</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayServiceAwsLogsConfiguration) -> dict:
    out: dict = {}
    out["logGroup"] = value["log_group"]
    out["logStreamPrefix"] = value["log_stream_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayServiceAwsLogsConfiguration:
    out: ExpressGatewayServiceAwsLogsConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroup" in data:
        out["log_group"] = data["logGroup"]
    else:
        raise DeserializationError(
            "ExpressGatewayServiceAwsLogsConfiguration.log_group required"
        )
    if "logStreamPrefix" in data:
        out["log_stream_prefix"] = data["logStreamPrefix"]
    else:
        raise DeserializationError(
            "ExpressGatewayServiceAwsLogsConfiguration.log_stream_prefix required"
        )
    return out
