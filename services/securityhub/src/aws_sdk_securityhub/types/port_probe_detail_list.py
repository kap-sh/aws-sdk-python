"""Generated from Smithy shape ``com.amazonaws.securityhub#PortProbeDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.port_probe_detail

PortProbeDetailList: TypeAlias = list[
    "aws_sdk_securityhub.types.port_probe_detail.PortProbeDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeDetailList) -> list:
    import aws_sdk_securityhub.types.port_probe_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.port_probe_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortProbeDetailList:
    import aws_sdk_securityhub.types.port_probe_detail

    out: PortProbeDetailList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.port_probe_detail.deserialize_json(item))
    return out
