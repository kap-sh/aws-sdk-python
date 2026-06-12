"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#CloudWatchLogsLogDeliveryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__boolean
    import aws_sdk_kafkaconnect.types.__string


class CloudWatchLogsLogDeliveryDescription(TypedDict):
    enabled: "aws_sdk_kafkaconnect.types.__boolean.__boolean"
    """<p>Whether log delivery to Amazon CloudWatch Logs is enabled.</p>"""
    log_group: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the CloudWatch log group that is the destination for log delivery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogsLogDeliveryDescription) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "log_group" in value:
        out["logGroup"] = value["log_group"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogsLogDeliveryDescription:
    out: CloudWatchLogsLogDeliveryDescription = {}  # type: ignore[typeddict-item]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if "logGroup" in data:
        out["log_group"] = data["logGroup"]
    return out
