"""Generated from Smithy shape ``com.amazonaws.mediatailor#SegmentDeliveryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__string


class SegmentDeliveryConfiguration(TypedDict):
    base_url: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>The base URL of the host or path of the segment delivery server that you're using to serve segments. This is typically a content delivery network (CDN). The URL can be absolute or relative. To use an absolute URL include the protocol, such as <code>https://example.com/some/path</code>. To use a relative URL specify the relative path, such as <code>/some/path*</code>.</p>"""
    name: NotRequired["aws_sdk_mediatailor.types.__string.__string"]
    """<p>A unique identifier used to distinguish between multiple segment delivery configurations in a source location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentDeliveryConfiguration) -> dict:
    out: dict = {}
    if "base_url" in value:
        out["BaseUrl"] = value["base_url"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SegmentDeliveryConfiguration:
    out: SegmentDeliveryConfiguration = {}  # type: ignore[typeddict-item]
    if "BaseUrl" in data:
        out["base_url"] = data["BaseUrl"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
