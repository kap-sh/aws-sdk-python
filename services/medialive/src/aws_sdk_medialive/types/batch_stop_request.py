"""Generated from Smithy shape ``com.amazonaws.medialive#BatchStopRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string


class BatchStopRequest(TypedDict):
    channel_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of channel IDs"""
    multiplex_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of multiplex IDs"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStopRequest) -> dict:
    out: dict = {}
    if "channel_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["channelIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["channel_ids"]
        )
    if "multiplex_ids" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["multiplexIds"] = aws_sdk_medialive.types.__list_of__string.serialize_json(
            value["multiplex_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchStopRequest:
    out: BatchStopRequest = {}  # type: ignore[typeddict-item]
    if "channelIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["channel_ids"] = aws_sdk_medialive.types.__list_of__string.deserialize_json(
            data["channelIds"]
        )
    if "multiplexIds" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["multiplex_ids"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["multiplexIds"]
            )
        )
    return out
