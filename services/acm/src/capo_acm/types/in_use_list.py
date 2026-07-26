"""Generated from Smithy shape ``com.amazonaws.acm#InUseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.string

InUseList: TypeAlias = list["capo_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InUseList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InUseList:
    return list(data)
