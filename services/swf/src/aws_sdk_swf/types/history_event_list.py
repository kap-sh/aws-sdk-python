"""Generated from Smithy shape ``com.amazonaws.swf#HistoryEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_swf.types.history_event

HistoryEventList: TypeAlias = list["aws_sdk_swf.types.history_event.HistoryEvent"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HistoryEventList) -> list:
    import aws_sdk_swf.types.history_event

    out: list = []
    for item in value:
        out.append(aws_sdk_swf.types.history_event.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HistoryEventList:
    import aws_sdk_swf.types.history_event

    out: HistoryEventList = []
    for item in data:
        out.append(aws_sdk_swf.types.history_event.deserialize_aws_json_1_0(item))
    return out
