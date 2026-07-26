"""Generated from Smithy shape ``com.amazonaws.comprehend#ListOfBlockReferences``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.block_reference

ListOfBlockReferences: TypeAlias = list[
    "capo_comprehend.types.block_reference.BlockReference"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfBlockReferences) -> list:
    import capo_comprehend.types.block_reference

    out: list = []
    for item in value:
        out.append(capo_comprehend.types.block_reference.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfBlockReferences:
    import capo_comprehend.types.block_reference

    out: ListOfBlockReferences = []
    for item in data:
        out.append(capo_comprehend.types.block_reference.deserialize_aws_json_1_1(item))
    return out
