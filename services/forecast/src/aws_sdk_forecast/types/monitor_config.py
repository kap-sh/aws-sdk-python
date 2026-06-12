"""Generated from Smithy shape ``com.amazonaws.forecast#MonitorConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.name


class MonitorConfig(TypedDict):
    monitor_name: "aws_sdk_forecast.types.name.Name"
    """<p>The name of the monitor resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitorConfig) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitorConfig:
    out: MonitorConfig = {}  # type: ignore[typeddict-item]
    if "MonitorName" in data:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("MonitorConfig.monitor_name required")
    return out
