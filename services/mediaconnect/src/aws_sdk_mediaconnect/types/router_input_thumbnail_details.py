"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputThumbnailDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mediaconnect.types.router_input_messages


class RouterInputThumbnailDetails(TypedDict):
    thumbnail_messages: (
        "aws_sdk_mediaconnect.types.router_input_messages.RouterInputMessages"
    )
    """<p>The messages associated with the router input thumbnail.</p>"""
    thumbnail: NotRequired["bytes"]
    """<p>The thumbnail image, encoded as a Base64-encoded binary data object.</p>"""
    timecode: NotRequired["str"]
    """<p>The timecode associated with the thumbnail.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp associated with the thumbnail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputThumbnailDetails) -> dict:
    out: dict = {}
    import aws_sdk_mediaconnect.types.router_input_messages

    out["thumbnailMessages"] = (
        aws_sdk_mediaconnect.types.router_input_messages.serialize_json(
            value["thumbnail_messages"]
        )
    )
    if "thumbnail" in value:
        import aws_sdk_mediaconnect.types._prelude.blob

        out["thumbnail"] = aws_sdk_mediaconnect.types._prelude.blob.serialize_json(
            value["thumbnail"]
        )
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    if "timestamp" in value:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["timestamp"] = aws_sdk_mediaconnect.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> RouterInputThumbnailDetails:
    out: RouterInputThumbnailDetails = {}  # type: ignore[typeddict-item]
    if "thumbnailMessages" in data:
        import aws_sdk_mediaconnect.types.router_input_messages

        out["thumbnail_messages"] = (
            aws_sdk_mediaconnect.types.router_input_messages.deserialize_json(
                data["thumbnailMessages"]
            )
        )
    else:
        raise DeserializationError(
            "RouterInputThumbnailDetails.thumbnail_messages required"
        )
    if "thumbnail" in data:
        import aws_sdk_mediaconnect.types._prelude.blob

        out["thumbnail"] = aws_sdk_mediaconnect.types._prelude.blob.deserialize_json(
            data["thumbnail"]
        )
    if "timecode" in data:
        out["timecode"] = data["timecode"]
    if "timestamp" in data:
        import aws_sdk_mediaconnect.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_mediaconnect.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    return out
