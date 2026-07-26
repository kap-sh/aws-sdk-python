"""Generated from Smithy shape ``com.amazonaws.marketplacemetering#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_metering.types.tag

TagList: TypeAlias = list["capo_marketplace_metering.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    import capo_marketplace_metering.types.tag

    out: list = []
    for item in value:
        out.append(capo_marketplace_metering.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagList:
    import capo_marketplace_metering.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_marketplace_metering.types.tag.deserialize_aws_json_1_1(item))
    return out
