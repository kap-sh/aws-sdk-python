"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfEntities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entity

ListOfEntities: TypeAlias = list["aws_sdk_comprehend.types.entity.Entity"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfEntities) -> list:
    import aws_sdk_comprehend.types.entity

    out: list = []
    for item in value:
        out.append(aws_sdk_comprehend.types.entity.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfEntities:
    import aws_sdk_comprehend.types.entity

    out: ListOfEntities = []
    for item in data:
        out.append(aws_sdk_comprehend.types.entity.deserialize_aws_json_1_1(item))
    return out
