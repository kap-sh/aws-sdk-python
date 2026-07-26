"""Generated from Smithy shape ``com.amazonaws.glue#Workflows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.workflow

Workflows: TypeAlias = list["capo_glue.types.workflow.Workflow"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workflows) -> list:
    import capo_glue.types.workflow

    out: list = []
    for item in value:
        out.append(capo_glue.types.workflow.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Workflows:
    import capo_glue.types.workflow

    out: Workflows = []
    for item in data:
        out.append(capo_glue.types.workflow.deserialize_aws_json_1_1(item))
    return out
