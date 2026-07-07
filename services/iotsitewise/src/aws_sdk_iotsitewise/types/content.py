"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Content``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.string


class Content(TypedDict, closed=True):
    text: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> Content:
    out: Content = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
