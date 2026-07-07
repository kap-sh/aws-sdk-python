"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PromotionalEmbeddedImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.non_empty_string
    import aws_sdk_marketplace_discovery.types.nullable_string
    import aws_sdk_marketplace_discovery.types.url


class PromotionalEmbeddedImage(TypedDict, closed=True):
    title: "aws_sdk_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The title displayed when hovering over the image.</p>"""
    url: "aws_sdk_marketplace_discovery.types.url.URL"
    """<p>The URL of the image file.</p>"""
    description: NotRequired[
        "aws_sdk_marketplace_discovery.types.nullable_string.NullableString"
    ]
    """<p>An optional description of the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromotionalEmbeddedImage) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["url"] = value["url"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> PromotionalEmbeddedImage:
    out: PromotionalEmbeddedImage = {}  # type: ignore[typeddict-item]
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("PromotionalEmbeddedImage.title required")
    if "url" in data:
        out["url"] = data["url"]
    else:
        raise DeserializationError("PromotionalEmbeddedImage.url required")
    if "description" in data:
        out["description"] = data["description"]
    return out
