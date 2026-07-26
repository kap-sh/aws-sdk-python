"""Generated from Smithy shape ``com.amazonaws.glue#ManyInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.node_id

ManyInputs: TypeAlias = list["capo_glue.types.node_id.NodeId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManyInputs) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ManyInputs:
    return list(data)
