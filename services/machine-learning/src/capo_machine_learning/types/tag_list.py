"""Generated from Smithy shape ``com.amazonaws.machinelearning#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.tag

TagList: TypeAlias = list["capo_machine_learning.types.tag.Tag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagList) -> list:
    import capo_machine_learning.types.tag

    out: list = []
    for item in value:
        out.append(capo_machine_learning.types.tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TagList:
    import capo_machine_learning.types.tag

    out: TagList = []
    for item in data:
        out.append(capo_machine_learning.types.tag.deserialize_aws_json_1_1(item))
    return out
