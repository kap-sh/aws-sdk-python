"""Generated from Smithy shape ``com.amazonaws.appconfig#MonitorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.monitor

MonitorList: TypeAlias = list["aws_sdk_appconfig.types.monitor.Monitor"]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorList) -> list:
    import aws_sdk_appconfig.types.monitor

    out: list = []
    for item in value:
        out.append(aws_sdk_appconfig.types.monitor.serialize_json(item))
    return out


def deserialize_json(data: list) -> MonitorList:
    import aws_sdk_appconfig.types.monitor

    out: MonitorList = []
    for item in data:
        out.append(aws_sdk_appconfig.types.monitor.deserialize_json(item))
    return out
