"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CloudWatchMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_emr_containers.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.log_group_name
    import aws_sdk_emr_containers.types.string256


class CloudWatchMonitoringConfiguration(TypedDict, closed=True):
    log_group_name: "aws_sdk_emr_containers.types.log_group_name.LogGroupName"
    """<p>The name of the log group for log publishing.</p>"""
    log_stream_name_prefix: NotRequired[
        "aws_sdk_emr_containers.types.string256.String256"
    ]
    """<p>The specified name prefix for log streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchMonitoringConfiguration) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    if "log_stream_name_prefix" in value:
        out["logStreamNamePrefix"] = value["log_stream_name_prefix"]
    return out


def deserialize_json(data: dict) -> CloudWatchMonitoringConfiguration:
    out: CloudWatchMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError(
            "CloudWatchMonitoringConfiguration.log_group_name required"
        )
    if "logStreamNamePrefix" in data:
        out["log_stream_name_prefix"] = data["logStreamNamePrefix"]
    return out
