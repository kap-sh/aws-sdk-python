"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.probe

ProbeList: TypeAlias = list["aws_sdk_networkmonitor.types.probe.Probe"]


# --- restJson1 ser/de ---
def serialize_json(value: ProbeList) -> list:
    import aws_sdk_networkmonitor.types.probe

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmonitor.types.probe.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProbeList:
    import aws_sdk_networkmonitor.types.probe

    out: ProbeList = []
    for item in data:
        out.append(aws_sdk_networkmonitor.types.probe.deserialize_json(item))
    return out
