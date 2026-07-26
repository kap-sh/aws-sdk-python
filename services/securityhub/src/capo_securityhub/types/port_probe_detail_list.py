"""Generated from Smithy shape ``com.amazonaws.securityhub#PortProbeDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.port_probe_detail

PortProbeDetailList: TypeAlias = list[
    "capo_securityhub.types.port_probe_detail.PortProbeDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeDetailList) -> list:
    import capo_securityhub.types.port_probe_detail

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.port_probe_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortProbeDetailList:
    import capo_securityhub.types.port_probe_detail

    out: PortProbeDetailList = []
    for item in data:
        out.append(capo_securityhub.types.port_probe_detail.deserialize_json(item))
    return out
