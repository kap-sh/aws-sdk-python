"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostAllocationTagsStatusErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error

UpdateCostAllocationTagsStatusErrors: TypeAlias = list[
    "aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error.UpdateCostAllocationTagsStatusError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostAllocationTagsStatusErrors) -> list:
    import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UpdateCostAllocationTagsStatusErrors:
    import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error

    out: UpdateCostAllocationTagsStatusErrors = []
    for item in data:
        out.append(
            aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_error.deserialize_aws_json_1_1(
                item
            )
        )
    return out
