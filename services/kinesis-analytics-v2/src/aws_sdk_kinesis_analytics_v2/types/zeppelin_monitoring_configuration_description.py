"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinMonitoringConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.log_level


class ZeppelinMonitoringConfigurationDescription(TypedDict):
    log_level: NotRequired["aws_sdk_kinesis_analytics_v2.types.log_level.LogLevel"]
    """<p>Describes the verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinMonitoringConfigurationDescription) -> dict:
    out: dict = {}
    if "log_level" in value:
        import aws_sdk_kinesis_analytics_v2.types.log_level

        out["LogLevel"] = (
            aws_sdk_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
                value["log_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinMonitoringConfigurationDescription:
    out: ZeppelinMonitoringConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import aws_sdk_kinesis_analytics_v2.types.log_level

        out["log_level"] = (
            aws_sdk_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    return out
