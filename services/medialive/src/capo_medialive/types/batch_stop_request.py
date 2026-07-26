"""Generated from Smithy shape ``com.amazonaws.medialive#BatchStopRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string


class BatchStopRequest(TypedDict, closed=True):
    channel_ids: NotRequired["capo_medialive.types.__list_of__string.__listOf__string"]
    """List of channel IDs"""
    multiplex_ids: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """List of multiplex IDs"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStopRequest) -> dict:
    out: dict = {}
    if "channel_ids" in value:
        import capo_medialive.types.__list_of__string

        out["channelIds"] = capo_medialive.types.__list_of__string.serialize_json(
            value["channel_ids"]
        )
    if "multiplex_ids" in value:
        import capo_medialive.types.__list_of__string

        out["multiplexIds"] = capo_medialive.types.__list_of__string.serialize_json(
            value["multiplex_ids"]
        )
    return out


def deserialize_json(data: dict) -> BatchStopRequest:
    out: BatchStopRequest = {}  # type: ignore[typeddict-item]
    if "channelIds" in data:
        import capo_medialive.types.__list_of__string

        out["channel_ids"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["channelIds"]
        )
    if "multiplexIds" in data:
        import capo_medialive.types.__list_of__string

        out["multiplex_ids"] = capo_medialive.types.__list_of__string.deserialize_json(
            data["multiplexIds"]
        )
    return out
