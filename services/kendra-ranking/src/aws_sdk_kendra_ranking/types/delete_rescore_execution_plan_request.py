"""Generated from Smithy shape ``com.amazonaws.kendraranking#DeleteRescoreExecutionPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_id


class DeleteRescoreExecutionPlanRequest(TypedDict, closed=True):
    id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    """<p>The identifier of the rescore execution plan that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRescoreExecutionPlanRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRescoreExecutionPlanRequest:
    out: DeleteRescoreExecutionPlanRequest = {}  # type: ignore[typeddict-item]
    return out
