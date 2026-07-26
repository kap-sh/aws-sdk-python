"""Generated from Smithy shape ``com.amazonaws.dax#SubnetGroupNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.string

SubnetGroupNameList: TypeAlias = list["capo_dax.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroupNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SubnetGroupNameList:
    return list(data)
