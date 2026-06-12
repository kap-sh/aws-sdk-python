"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.list_workflows_item

WorkflowList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.list_workflows_item.ListWorkflowsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowList) -> list:
    import aws_sdk_customer_profiles.types.list_workflows_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_customer_profiles.types.list_workflows_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowList:
    import aws_sdk_customer_profiles.types.list_workflows_item

    out: WorkflowList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.list_workflows_item.deserialize_json(item)
        )
    return out
