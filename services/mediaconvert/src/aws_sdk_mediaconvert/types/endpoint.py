"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Endpoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string


class Endpoint(TypedDict):
    url: NotRequired["aws_sdk_mediaconvert.types.__string.__string"]
    """URL of endpoint"""


# --- restJson1 ser/de ---
def serialize_json(value: Endpoint) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if "url" in data:
        out["url"] = data["url"]
    return out
