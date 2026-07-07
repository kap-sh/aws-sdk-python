"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostAllocationTagsStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors


class UpdateCostAllocationTagsStatusResponse(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors.UpdateCostAllocationTagsStatusErrors"
    ]
    """<p>A list of <code>UpdateCostAllocationTagsStatusError</code> objects with error details about each cost allocation tag that can't be updated. If there's no failure, an empty array returns. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostAllocationTagsStatusResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors

        out["Errors"] = (
            aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostAllocationTagsStatusResponse:
    out: UpdateCostAllocationTagsStatusResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors

        out["errors"] = (
            aws_sdk_cost_explorer.types.update_cost_allocation_tags_status_errors.deserialize_aws_json_1_1(
                data["Errors"]
            )
        )
    return out
