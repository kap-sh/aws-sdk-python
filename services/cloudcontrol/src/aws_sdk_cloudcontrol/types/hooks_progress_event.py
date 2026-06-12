"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#HooksProgressEvent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.hook_progress_event

HooksProgressEvent: TypeAlias = list[
    "aws_sdk_cloudcontrol.types.hook_progress_event.HookProgressEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HooksProgressEvent) -> list:
    import aws_sdk_cloudcontrol.types.hook_progress_event

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudcontrol.types.hook_progress_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> HooksProgressEvent:
    import aws_sdk_cloudcontrol.types.hook_progress_event

    out: HooksProgressEvent = []
    for item in data:
        out.append(
            aws_sdk_cloudcontrol.types.hook_progress_event.deserialize_aws_json_1_0(
                item
            )
        )
    return out
