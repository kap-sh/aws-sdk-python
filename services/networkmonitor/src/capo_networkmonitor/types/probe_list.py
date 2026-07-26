"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmonitor.types.probe

ProbeList: TypeAlias = list["capo_networkmonitor.types.probe.Probe"]


# --- restJson1 ser/de ---
def serialize_json(value: ProbeList) -> list:
    import capo_networkmonitor.types.probe

    out: list = []
    for item in value:
        out.append(capo_networkmonitor.types.probe.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProbeList:
    import capo_networkmonitor.types.probe

    out: ProbeList = []
    for item in data:
        out.append(capo_networkmonitor.types.probe.deserialize_json(item))
    return out
