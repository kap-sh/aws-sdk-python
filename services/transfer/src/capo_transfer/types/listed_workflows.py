"""Generated from Smithy shape ``com.amazonaws.transfer#ListedWorkflows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.listed_workflow

ListedWorkflows: TypeAlias = list["capo_transfer.types.listed_workflow.ListedWorkflow"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedWorkflows) -> list:
    import capo_transfer.types.listed_workflow

    out: list = []
    for item in value:
        out.append(capo_transfer.types.listed_workflow.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListedWorkflows:
    import capo_transfer.types.listed_workflow

    out: ListedWorkflows = []
    for item in data:
        out.append(capo_transfer.types.listed_workflow.deserialize_aws_json_1_1(item))
    return out
