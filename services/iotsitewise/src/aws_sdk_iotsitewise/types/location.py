"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Location``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.string


class Location(TypedDict):
    uri: NotRequired["aws_sdk_iotsitewise.types.string.String"]
    """<p>The URI of the location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    return out
