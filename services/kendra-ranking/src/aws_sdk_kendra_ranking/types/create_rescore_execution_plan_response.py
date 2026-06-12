"""Generated from Smithy shape ``com.amazonaws.kendraranking#CreateRescoreExecutionPlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kendra_ranking.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_arn
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_id


class CreateRescoreExecutionPlanResponse(TypedDict):
    id: "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    """<p>The identifier of the rescore execution plan.</p>"""
    arn: "aws_sdk_kendra_ranking.types.rescore_execution_plan_arn.RescoreExecutionPlanArn"
    """<p>The Amazon Resource Name (ARN) of the rescore execution plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRescoreExecutionPlanResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRescoreExecutionPlanResponse:
    out: CreateRescoreExecutionPlanResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CreateRescoreExecutionPlanResponse.id required")
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CreateRescoreExecutionPlanResponse.arn required")
    return out
