"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ImageLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.id
    import aws_sdk_iotsitewise.types.url


class ImageLocation(TypedDict, closed=True):
    id: "aws_sdk_iotsitewise.types.id.ID"
    """<p>The ID of the image.</p>"""
    url: "aws_sdk_iotsitewise.types.url.Url"
    """<p>The URL where the image is available. The URL is valid for 15 minutes so that you can view and download the image</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLocation) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> ImageLocation:
    out: ImageLocation = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ImageLocation.id required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("ImageLocation.url required")
    return out
