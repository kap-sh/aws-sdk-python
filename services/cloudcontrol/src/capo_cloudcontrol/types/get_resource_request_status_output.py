"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceRequestStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudcontrol.types.hooks_progress_event
    import capo_cloudcontrol.types.progress_event


class GetResourceRequestStatusOutput(TypedDict, closed=True):
    progress_event: NotRequired["capo_cloudcontrol.types.progress_event.ProgressEvent"]
    """<p>Represents the current status of the resource operation request.</p>"""
    hooks_progress_event: NotRequired[
        "capo_cloudcontrol.types.hooks_progress_event.HooksProgressEvent"
    ]
    """<p>Lists Hook invocations for the specified target in the request. This is a list since the same target can invoke multiple Hooks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceRequestStatusOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import capo_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            capo_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    if "hooks_progress_event" in value:
        import capo_cloudcontrol.types.hooks_progress_event

        out["HooksProgressEvent"] = (
            capo_cloudcontrol.types.hooks_progress_event.serialize_aws_json_1_0(
                value["hooks_progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceRequestStatusOutput:
    out: GetResourceRequestStatusOutput = {}  # type: ignore[typeddict-item]
    if "ProgressEvent" in data:
        import capo_cloudcontrol.types.progress_event

        out["progress_event"] = (
            capo_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    if "HooksProgressEvent" in data:
        import capo_cloudcontrol.types.hooks_progress_event

        out["hooks_progress_event"] = (
            capo_cloudcontrol.types.hooks_progress_event.deserialize_aws_json_1_0(
                data["HooksProgressEvent"]
            )
        )
    return out
