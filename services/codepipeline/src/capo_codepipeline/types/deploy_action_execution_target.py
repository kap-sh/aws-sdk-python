"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployActionExecutionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.deploy_target_event_list
    import capo_codepipeline.types.string
    import capo_codepipeline.types.timestamp


class DeployActionExecutionTarget(TypedDict, closed=True):
    target_id: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The ID of the target for the deploy action.</p>"""
    target_type: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The type of target for the deploy action.</p>"""
    status: NotRequired["capo_codepipeline.types.string.String"]
    """<p>The status of the deploy action.</p>"""
    start_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time for the deploy action.</p>"""
    end_time: NotRequired["capo_codepipeline.types.timestamp.Timestamp"]
    """<p>The end time for the deploy action.</p>"""
    events: NotRequired[
        "capo_codepipeline.types.deploy_target_event_list.DeployTargetEventList"
    ]
    """<p>The lifecycle events for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployActionExecutionTarget) -> dict:
    out: dict = {}
    if "target_id" in value:
        out["targetId"] = value["target_id"]
    if "target_type" in value:
        out["targetType"] = value["target_type"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import capo_codepipeline.types.timestamp

        out["startTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codepipeline.types.timestamp

        out["endTime"] = capo_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "events" in value:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = (
            capo_codepipeline.types.deploy_target_event_list.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployActionExecutionTarget:
    out: DeployActionExecutionTarget = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    if "targetType" in data:
        out["target_type"] = data["targetType"]
    if "status" in data:
        out["status"] = data["status"]
    if "startTime" in data:
        import capo_codepipeline.types.timestamp

        out["start_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if "endTime" in data:
        import capo_codepipeline.types.timestamp

        out["end_time"] = capo_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "events" in data:
        import capo_codepipeline.types.deploy_target_event_list

        out["events"] = (
            capo_codepipeline.types.deploy_target_event_list.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    return out
