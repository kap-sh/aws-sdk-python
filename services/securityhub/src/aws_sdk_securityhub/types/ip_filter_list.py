"""Generated from Smithy shape ``com.amazonaws.securityhub#IpFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ip_filter

IpFilterList: TypeAlias = list["aws_sdk_securityhub.types.ip_filter.IpFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: IpFilterList) -> list:
    import aws_sdk_securityhub.types.ip_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.ip_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IpFilterList:
    import aws_sdk_securityhub.types.ip_filter

    out: IpFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.ip_filter.deserialize_json(item))
    return out
