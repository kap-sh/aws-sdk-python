"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#CancelResourceRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.progress_event


class CancelResourceRequestOutput(TypedDict, closed=True):
    progress_event: NotRequired[
        "aws_sdk_cloudcontrol.types.progress_event.ProgressEvent"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelResourceRequestOutput) -> dict:
    out: dict = {}
    if "progress_event" in value:
        import aws_sdk_cloudcontrol.types.progress_event

        out["ProgressEvent"] = (
            aws_sdk_cloudcontrol.types.progress_event.serialize_aws_json_1_0(
                value["progress_event"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelResourceRequestOutput:
    out: CancelResourceRequestOutput = {}  # type: ignore[typeddict-item]
    if "ProgressEvent" in data:
        import aws_sdk_cloudcontrol.types.progress_event

        out["progress_event"] = (
            aws_sdk_cloudcontrol.types.progress_event.deserialize_aws_json_1_0(
                data["ProgressEvent"]
            )
        )
    return out
