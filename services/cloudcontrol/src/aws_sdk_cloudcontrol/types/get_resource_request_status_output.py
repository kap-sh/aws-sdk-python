"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceRequestStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.hooks_progress_event
    import aws_sdk_cloudcontrol.types.progress_event


class GetResourceRequestStatusOutput(TypedDict):
    progress_event: NotRequired[
        "aws_sdk_cloudcontrol.types.progress_event.ProgressEvent"
    ]
    """<p>Represents the current status of the resource operation request.</p>"""
    hooks_progress_event: NotRequired[
        "aws_sdk_cloudcontrol.types.hooks_progress_event.HooksProgressEvent"
    ]
    """<p>Lists Hook invocations for the specified target in the request. This is a list since the same target can invoke multiple Hooks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceRequestStatusOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import aws_sdk_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            aws_sdk_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    if "hooks_progress_event" in value:
        import aws_sdk_cloudcontrol.types.hooks_progress_event

        out["HooksProgressEvent"] = (
            aws_sdk_cloudcontrol.types.hooks_progress_event.serialize_aws_json_1_0(
                value["hooks_progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceRequestStatusOutput:
    out: GetResourceRequestStatusOutput = {}  # type: ignore[typeddict-item]
    if "ProgressEvent" in data:
        import aws_sdk_cloudcontrol.types.progress_event

        out["progress_event"] = (
            aws_sdk_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    if "HooksProgressEvent" in data:
        import aws_sdk_cloudcontrol.types.hooks_progress_event

        out["hooks_progress_event"] = (
            aws_sdk_cloudcontrol.types.hooks_progress_event.deserialize_aws_json_1_0(
                data["HooksProgressEvent"]
            )
        )
    return out
