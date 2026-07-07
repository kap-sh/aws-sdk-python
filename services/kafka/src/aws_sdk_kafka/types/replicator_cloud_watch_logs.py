"""Generated from Smithy shape ``com.amazonaws.kafka#ReplicatorCloudWatchLogs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean
    import aws_sdk_kafka.types.__string


class ReplicatorCloudWatchLogs(TypedDict, closed=True):
    enabled: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Whether log delivery to CloudWatch Logs is enabled.</p>"""
    log_group: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The CloudWatch log group that is the destination for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicatorCloudWatchLogs) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "log_group" in value:
        out["logGroup"] = value["log_group"]
    return out


def deserialize_json(data: dict) -> ReplicatorCloudWatchLogs:
    out: ReplicatorCloudWatchLogs = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "logGroup" in data:
        out["log_group"] = data["logGroup"]
    return out
