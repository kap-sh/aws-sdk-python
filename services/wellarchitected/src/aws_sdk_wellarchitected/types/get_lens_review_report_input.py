"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetLensReviewReportInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.lens_alias
    import aws_sdk_wellarchitected.types.milestone_number
    import aws_sdk_wellarchitected.types.workload_id


class GetLensReviewReportInput(TypedDict):
    workload_id: "aws_sdk_wellarchitected.types.workload_id.WorkloadId"
    lens_alias: "aws_sdk_wellarchitected.types.lens_alias.LensAlias"
    milestone_number: NotRequired[
        "aws_sdk_wellarchitected.types.milestone_number.MilestoneNumber"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetLensReviewReportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLensReviewReportInput:
    out: GetLensReviewReportInput = {}  # type: ignore[typeddict-item]
    return out
