"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#EbsGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.ebs_group

EbsGroupList: TypeAlias = list["aws_sdk_accessanalyzer.types.ebs_group.EbsGroup"]


# --- restJson1 ser/de ---
def serialize_json(value: EbsGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> EbsGroupList:
    return list(data)
