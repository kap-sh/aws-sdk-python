"""Generated from Smithy shape ``com.amazonaws.iotdataplane#RetainedMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_data_plane.types.retained_message_summary

RetainedMessageList: TypeAlias = list[
    "aws_sdk_iot_data_plane.types.retained_message_summary.RetainedMessageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetainedMessageList) -> list:
    import aws_sdk_iot_data_plane.types.retained_message_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_data_plane.types.retained_message_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetainedMessageList:
    import aws_sdk_iot_data_plane.types.retained_message_summary

    out: RetainedMessageList = []
    for item in data:
        out.append(
            aws_sdk_iot_data_plane.types.retained_message_summary.deserialize_json(item)
        )
    return out
