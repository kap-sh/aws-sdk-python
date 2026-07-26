"""Generated from Smithy shape ``com.amazonaws.glue#PredecessorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.predecessor

PredecessorList: TypeAlias = list["capo_glue.types.predecessor.Predecessor"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredecessorList) -> list:
    import capo_glue.types.predecessor

    out: list = []
    for item in value:
        out.append(capo_glue.types.predecessor.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PredecessorList:
    import capo_glue.types.predecessor

    out: PredecessorList = []
    for item in data:
        out.append(capo_glue.types.predecessor.deserialize_aws_json_1_1(item))
    return out
