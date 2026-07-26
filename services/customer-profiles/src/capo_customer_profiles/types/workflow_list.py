"""Generated from Smithy shape ``com.amazonaws.customerprofiles#WorkflowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_workflows_item

WorkflowList: TypeAlias = list[
    "capo_customer_profiles.types.list_workflows_item.ListWorkflowsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowList) -> list:
    import capo_customer_profiles.types.list_workflows_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_workflows_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WorkflowList:
    import capo_customer_profiles.types.list_workflows_item

    out: WorkflowList = []
    for item in data:
        out.append(
            capo_customer_profiles.types.list_workflows_item.deserialize_json(item)
        )
    return out
