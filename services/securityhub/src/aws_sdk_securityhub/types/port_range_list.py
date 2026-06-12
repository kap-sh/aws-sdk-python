"""Generated from Smithy shape ``com.amazonaws.securityhub#PortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.port_range

PortRangeList: TypeAlias = list["aws_sdk_securityhub.types.port_range.PortRange"]


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeList) -> list:
    import aws_sdk_securityhub.types.port_range

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.port_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortRangeList:
    import aws_sdk_securityhub.types.port_range

    out: PortRangeList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.port_range.deserialize_json(item))
    return out
