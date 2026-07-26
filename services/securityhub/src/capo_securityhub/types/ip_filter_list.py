"""Generated from Smithy shape ``com.amazonaws.securityhub#IpFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ip_filter

IpFilterList: TypeAlias = list["capo_securityhub.types.ip_filter.IpFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: IpFilterList) -> list:
    import capo_securityhub.types.ip_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ip_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> IpFilterList:
    import capo_securityhub.types.ip_filter

    out: IpFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ip_filter.deserialize_json(item))
    return out
