"""Generated from Smithy shape ``com.amazonaws.codepipeline#DeployTargetEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.deploy_target_event_context
    import aws_sdk_codepipeline.types.string
    import aws_sdk_codepipeline.types.timestamp


class DeployTargetEvent(TypedDict):
    name: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The name of the event for the deploy action.</p>"""
    status: NotRequired["aws_sdk_codepipeline.types.string.String"]
    """<p>The status of the event for the deploy action.</p>"""
    start_time: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The start time for the event for the deploy action.</p>"""
    end_time: NotRequired["aws_sdk_codepipeline.types.timestamp.Timestamp"]
    """<p>The end time for the event for the deploy action.</p>"""
    context: NotRequired[
        "aws_sdk_codepipeline.types.deploy_target_event_context.DeployTargetEventContext"
    ]
    """<p>The context for the event for the deploy action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployTargetEvent) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        out["status"] = value["status"]
    if "start_time" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["startTime"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_codepipeline.types.timestamp

        out["endTime"] = aws_sdk_codepipeline.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "context" in value:
        import aws_sdk_codepipeline.types.deploy_target_event_context

        out["context"] = (
            aws_sdk_codepipeline.types.deploy_target_event_context.serialize_aws_json_1_1(
                value["context"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployTargetEvent:
    out: DeployTargetEvent = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        out["status"] = data["status"]
    if "startTime" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["start_time"] = (
            aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_codepipeline.types.timestamp

        out["end_time"] = aws_sdk_codepipeline.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if "context" in data:
        import aws_sdk_codepipeline.types.deploy_target_event_context

        out["context"] = (
            aws_sdk_codepipeline.types.deploy_target_event_context.deserialize_aws_json_1_1(
                data["context"]
            )
        )
    return out
