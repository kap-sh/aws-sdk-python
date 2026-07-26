"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinMonitoringConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.log_level


class ZeppelinMonitoringConfigurationDescription(TypedDict, closed=True):
    log_level: NotRequired["capo_kinesis_analytics_v2.types.log_level.LogLevel"]
    """<p>Describes the verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinMonitoringConfigurationDescription) -> dict:
    out: dict = {}
    if "log_level" in value:
        import capo_kinesis_analytics_v2.types.log_level

        out["LogLevel"] = (
            capo_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
                value["log_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinMonitoringConfigurationDescription:
    out: ZeppelinMonitoringConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import capo_kinesis_analytics_v2.types.log_level

        out["log_level"] = (
            capo_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    return out
