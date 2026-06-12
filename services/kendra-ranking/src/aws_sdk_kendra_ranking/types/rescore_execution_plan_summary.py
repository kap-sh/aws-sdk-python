"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreExecutionPlanSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_id
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_name
    import aws_sdk_kendra_ranking.types.rescore_execution_plan_status
    import aws_sdk_kendra_ranking.types.timestamp


class RescoreExecutionPlanSummary(TypedDict):
    name: NotRequired[
        "aws_sdk_kendra_ranking.types.rescore_execution_plan_name.RescoreExecutionPlanName"
    ]
    """<p>The name of the rescore execution plan.</p>"""
    id: NotRequired[
        "aws_sdk_kendra_ranking.types.rescore_execution_plan_id.RescoreExecutionPlanId"
    ]
    """<p>The identifier of the rescore execution plan.</p>"""
    created_at: NotRequired["aws_sdk_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the rescore execution plan was created.</p>"""
    updated_at: NotRequired["aws_sdk_kendra_ranking.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the rescore execution plan was last updated.</p>"""
    status: NotRequired[
        "aws_sdk_kendra_ranking.types.rescore_execution_plan_status.RescoreExecutionPlanStatus"
    ]
    """<p>The current status of the rescore execution plan. When the value is <code>ACTIVE</code>, the rescore execution plan is ready for use.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreExecutionPlanSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "created_at" in value:
        import aws_sdk_kendra_ranking.types.timestamp

        out["CreatedAt"] = (
            aws_sdk_kendra_ranking.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_kendra_ranking.types.timestamp

        out["UpdatedAt"] = (
            aws_sdk_kendra_ranking.types.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "status" in value:
        import aws_sdk_kendra_ranking.types.rescore_execution_plan_status

        out["Status"] = (
            aws_sdk_kendra_ranking.types.rescore_execution_plan_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreExecutionPlanSummary:
    out: RescoreExecutionPlanSummary = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatedAt" in data:
        import aws_sdk_kendra_ranking.types.timestamp

        out["created_at"] = (
            aws_sdk_kendra_ranking.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "UpdatedAt" in data:
        import aws_sdk_kendra_ranking.types.timestamp

        out["updated_at"] = (
            aws_sdk_kendra_ranking.types.timestamp.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    if "Status" in data:
        import aws_sdk_kendra_ranking.types.rescore_execution_plan_status

        out["status"] = (
            aws_sdk_kendra_ranking.types.rescore_execution_plan_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
