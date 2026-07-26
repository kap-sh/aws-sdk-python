"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.tag

TagList: TypeAlias = list["capo_partnercentral_selling.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagList) -> list:
    import capo_partnercentral_selling.types.tag

    out: list = []
    for item in value:
        out.append(capo_partnercentral_selling.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> TagList:
    import capo_partnercentral_selling.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_partnercentral_selling.types.tag.deserialize_aws_json_1_0(item))
    return out
