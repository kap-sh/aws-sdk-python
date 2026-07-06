"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiMediaInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info


class NdiMediaInfo(TypedDict, closed=True):
    streams: NotRequired[
        "aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info.__listOfNdiMediaStreamInfo"
    ]
    """<p> A list of the individual media streams that make up the NDI source. This includes details about each stream's codec, resolution, frame rate, audio channels, and other parameters. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiMediaInfo) -> dict:
    out: dict = {}
    if "streams" in value:
        import aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info

        out["streams"] = (
            aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info.serialize_json(
                value["streams"]
            )
        )
    return out


def deserialize_json(data: dict) -> NdiMediaInfo:
    out: NdiMediaInfo = {}  # type: ignore[typeddict-item]
    if "streams" in data:
        import aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info

        out["streams"] = (
            aws_sdk_mediaconnect.types.__list_of_ndi_media_stream_info.deserialize_json(
                data["streams"]
            )
        )
    return out
