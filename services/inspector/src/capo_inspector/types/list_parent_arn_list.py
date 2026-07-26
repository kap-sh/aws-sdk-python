"""Generated from Smithy shape ``com.amazonaws.inspector#ListParentArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector.types.arn

ListParentArnList: TypeAlias = list["capo_inspector.types.arn.Arn"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListParentArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListParentArnList:
    return list(data)
