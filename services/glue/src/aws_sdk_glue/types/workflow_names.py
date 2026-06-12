"""Generated from Smithy shape ``com.amazonaws.glue#WorkflowNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.name_string

WorkflowNames: TypeAlias = list["aws_sdk_glue.types.name_string.NameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> WorkflowNames:
    return list(data)
