"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#HooksProgressEvent``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudcontrol.types.hook_progress_event

HooksProgressEvent: TypeAlias = list[
    "capo_cloudcontrol.types.hook_progress_event.HookProgressEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HooksProgressEvent) -> list:
    import capo_cloudcontrol.types.hook_progress_event

    out: list = []
    for item in value:
        out.append(
            capo_cloudcontrol.types.hook_progress_event.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> HooksProgressEvent:
    import capo_cloudcontrol.types.hook_progress_event

    out: HooksProgressEvent = []
    for item in data:
        out.append(
            capo_cloudcontrol.types.hook_progress_event.deserialize_aws_json_1_0(item)
        )
    return out
