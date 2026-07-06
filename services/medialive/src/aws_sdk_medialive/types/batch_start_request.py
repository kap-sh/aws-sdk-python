"""Generated from Smithy shape ``com.amazonaws.medialive#BatchStartRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string


class BatchStartRequest(TypedDict, closed=True):
    channel_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of channel IDs"""
    multiplex_ids: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of multiplex IDs"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartRequest) -> dict:
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


def deserialize_json(data: dict) -> BatchStartRequest:
    out: BatchStartRequest = {}  # type: ignore[typeddict-item]
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
