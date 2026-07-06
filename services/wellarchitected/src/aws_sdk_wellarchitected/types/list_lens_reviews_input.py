"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListLensReviewsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.max_results
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.next_token
    import aws_sdk_wellarchitected.types.workload_id


class ListLensReviewsInput(TypedDict, closed=True):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]
    next_token: NotRequired["aws_sdk_wellarchitected.types.next_token.NextToken"]
    max_results: NotRequired["aws_sdk_wellarchitected.types.max_results.MaxResults"]


# --- restJson1 ser/de ---
def serialize_json(value: ListLensReviewsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLensReviewsInput:
    out: ListLensReviewsInput = {}  # type: ignore[typeddict-item]
    return out
