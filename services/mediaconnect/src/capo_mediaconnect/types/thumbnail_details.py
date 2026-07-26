"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ThumbnailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__list_of_message_detail


class ThumbnailDetails(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p> The ARN of the flow that DescribeFlowSourceThumbnail was performed on.</p>"""
    thumbnail: NotRequired["str"]
    """<p>Thumbnail Base64 string. </p>"""
    thumbnail_messages: NotRequired[
        "capo_mediaconnect.types.__list_of_message_detail.__listOfMessageDetail"
    ]
    """<p> Status code and messages about the flow source thumbnail.</p>"""
    timecode: NotRequired["str"]
    """<p> Timecode of thumbnail.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of when thumbnail was generated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThumbnailDetails) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "thumbnail" in value:
        out["thumbnail"] = value["thumbnail"]
    if "thumbnail_messages" in value:
        import capo_mediaconnect.types.__list_of_message_detail

        out["thumbnailMessages"] = (
            capo_mediaconnect.types.__list_of_message_detail.serialize_json(
                value["thumbnail_messages"]
            )
        )
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    if "timestamp" in value:
        import capo_mediaconnect.types._prelude.timestamp

        out["timestamp"] = capo_mediaconnect.types._prelude.timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> ThumbnailDetails:
    out: ThumbnailDetails = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "thumbnail" in data:
        out["thumbnail"] = data["thumbnail"]
    if "thumbnailMessages" in data:
        import capo_mediaconnect.types.__list_of_message_detail

        out["thumbnail_messages"] = (
            capo_mediaconnect.types.__list_of_message_detail.deserialize_json(
                data["thumbnailMessages"]
            )
        )
    if "timecode" in data:
        out["timecode"] = data["timecode"]
    if "timestamp" in data:
        import capo_mediaconnect.types._prelude.timestamp

        out["timestamp"] = capo_mediaconnect.types._prelude.timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
