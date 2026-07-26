"""Generated from Smithy shape ``com.amazonaws.dax#NodeIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dax.types.string

NodeIdentifierList: TypeAlias = list["capo_dax.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NodeIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> NodeIdentifierList:
    return list(data)
