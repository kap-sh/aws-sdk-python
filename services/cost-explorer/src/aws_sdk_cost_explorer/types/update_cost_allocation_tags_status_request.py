"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostAllocationTagsStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status_list


class UpdateCostAllocationTagsStatusRequest(TypedDict, closed=True):
    cost_allocation_tags_status: "aws_sdk_cost_explorer.types.cost_allocation_tag_status_list.CostAllocationTagStatusList"
    """<p>The list of <code>CostAllocationTagStatusEntry</code> objects that are used to update cost allocation tags status for this request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostAllocationTagsStatusRequest) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.cost_allocation_tag_status_list

    out["CostAllocationTagsStatus"] = (
        aws_sdk_cost_explorer.types.cost_allocation_tag_status_list.serialize_aws_json_1_1(
            value["cost_allocation_tags_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostAllocationTagsStatusRequest:
    out: UpdateCostAllocationTagsStatusRequest = {}  # type: ignore[typeddict-item]
    if "CostAllocationTagsStatus" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_status_list

        out["cost_allocation_tags_status"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_status_list.deserialize_aws_json_1_1(
                data["CostAllocationTagsStatus"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCostAllocationTagsStatusRequest.cost_allocation_tags_status required"
        )
    return out
