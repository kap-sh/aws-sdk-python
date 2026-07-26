"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfIpFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.ocsf_ip_filter

OcsfIpFilterList: TypeAlias = list["capo_securityhub.types.ocsf_ip_filter.OcsfIpFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfIpFilterList) -> list:
    import capo_securityhub.types.ocsf_ip_filter

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.ocsf_ip_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfIpFilterList:
    import capo_securityhub.types.ocsf_ip_filter

    out: OcsfIpFilterList = []
    for item in data:
        out.append(capo_securityhub.types.ocsf_ip_filter.deserialize_json(item))
    return out
