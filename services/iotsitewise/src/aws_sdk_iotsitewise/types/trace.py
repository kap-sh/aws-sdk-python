"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Trace``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.string


class Trace(TypedDict):
    text: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The cited text from the data source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Trace) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    return out


def deserialize_json(data: dict) -> Trace:
    out: Trace = {}  # type: ignore[typeddict-item]
    if "text" in data:
        out["text"] = data["text"]
    return out
