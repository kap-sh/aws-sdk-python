"""Generated from Smithy shape ``com.amazonaws.athena#CloudWatchLoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.boxed_boolean
    import aws_sdk_athena.types.log_group_name
    import aws_sdk_athena.types.log_stream_name_prefix
    import aws_sdk_athena.types.log_types_map


class CloudWatchLoggingConfiguration(TypedDict, closed=True):
    enabled: "aws_sdk_athena.types.boxed_boolean.BoxedBoolean"
    """<p>Enables CloudWatch logging.</p>"""
    log_group: NotRequired["aws_sdk_athena.types.log_group_name.LogGroupName"]
    """<p>The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.</p>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_athena.types.log_stream_name_prefix.LogStreamNamePrefix"
    ]
    """<p>Prefix for the CloudWatch log stream name.</p>"""
    log_types: NotRequired["aws_sdk_athena.types.log_types_map.LogTypesMap"]
    """<p>The types of logs that you want to publish to CloudWatch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudWatchLoggingConfiguration) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "log_group" in value:
        out["LogGroup"] = value["log_group"]
    if "log_stream_name_prefix" in value:
        out["LogStreamNamePrefix"] = value["log_stream_name_prefix"]
    if "log_types" in value:
        import aws_sdk_athena.types.log_types_map

        out["LogTypes"] = aws_sdk_athena.types.log_types_map.serialize_aws_json_1_1(
            value["log_types"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudWatchLoggingConfiguration:
    out: CloudWatchLoggingConfiguration = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("CloudWatchLoggingConfiguration.enabled required")
    if "LogGroup" in data:
        out["log_group"] = data["LogGroup"]
    if "LogStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["LogStreamNamePrefix"]
    if "LogTypes" in data:
        import aws_sdk_athena.types.log_types_map

        out["log_types"] = aws_sdk_athena.types.log_types_map.deserialize_aws_json_1_1(
            data["LogTypes"]
        )
    return out
