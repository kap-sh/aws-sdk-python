"""Generated from Smithy shape ``com.amazonaws.swf#DomainInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_swf.types.domain_info

DomainInfoList: TypeAlias = list["capo_swf.types.domain_info.DomainInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainInfoList) -> list:
    import capo_swf.types.domain_info

    out: list = []
    for item in value:
        out.append(capo_swf.types.domain_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DomainInfoList:
    import capo_swf.types.domain_info

    out: DomainInfoList = []
    for item in data:
        out.append(capo_swf.types.domain_info.deserialize_aws_json_1_0(item))
    return out
