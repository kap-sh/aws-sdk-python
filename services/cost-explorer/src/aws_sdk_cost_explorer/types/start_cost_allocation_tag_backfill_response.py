"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartCostAllocationTagBackfillResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request


class StartCostAllocationTagBackfillResponse(TypedDict, closed=True):
    backfill_request: NotRequired[
        "aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request.CostAllocationTagBackfillRequest"
    ]
    """<p> An object containing detailed metadata of your new backfill request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCostAllocationTagBackfillResponse) -> dict:
    out: dict = {}
    if "backfill_request" in value:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request

        out["BackfillRequest"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request.serialize_aws_json_1_1(
                value["backfill_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCostAllocationTagBackfillResponse:
    out: StartCostAllocationTagBackfillResponse = {}  # type: ignore[typeddict-item]
    if "BackfillRequest" in data:
        import aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request

        out["backfill_request"] = (
            aws_sdk_cost_explorer.types.cost_allocation_tag_backfill_request.deserialize_aws_json_1_1(
                data["BackfillRequest"]
            )
        )
    return out
