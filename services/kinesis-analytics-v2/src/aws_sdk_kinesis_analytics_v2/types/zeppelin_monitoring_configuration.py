"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZeppelinMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.log_level


class ZeppelinMonitoringConfiguration(TypedDict, closed=True):
    log_level: "aws_sdk_kinesis_analytics_v2.types.log_level.LogLevel"
    """<p>The verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZeppelinMonitoringConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.log_level

    out["LogLevel"] = (
        aws_sdk_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
            value["log_level"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ZeppelinMonitoringConfiguration:
    out: ZeppelinMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "LogLevel" in data:
        import aws_sdk_kinesis_analytics_v2.types.log_level

        out["log_level"] = (
            aws_sdk_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    else:
        raise DeserializationError("ZeppelinMonitoringConfiguration.log_level required")
    return out
