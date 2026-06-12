"""Generated from Smithy shape ``com.amazonaws.securityhub#OcsfIpFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.ocsf_ip_filter

OcsfIpFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.ocsf_ip_filter.OcsfIpFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: OcsfIpFilterList) -> list:
    import aws_sdk_securityhub.types.ocsf_ip_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.ocsf_ip_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> OcsfIpFilterList:
    import aws_sdk_securityhub.types.ocsf_ip_filter

    out: OcsfIpFilterList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.ocsf_ip_filter.deserialize_json(item))
    return out
