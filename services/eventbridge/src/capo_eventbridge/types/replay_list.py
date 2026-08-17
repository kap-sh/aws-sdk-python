"""Generated from Smithy shape ``com.amazonaws.eventbridge#ReplayList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.replay

ReplayList: TypeAlias = list["capo_eventbridge.types.replay.Replay"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplayList) -> list:
    import capo_eventbridge.types.replay

    out: list = []
    for item in value:
        out.append(capo_eventbridge.types.replay.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReplayList:
    import capo_eventbridge.types.replay

    out: ReplayList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridge.types.replay.deserialize_aws_json_1_1(item))
    return out
