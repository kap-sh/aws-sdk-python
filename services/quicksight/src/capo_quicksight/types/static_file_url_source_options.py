"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFileUrlSourceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.string


class StaticFileUrlSourceOptions(TypedDict, closed=True):
    url: "capo_quicksight.types.string.String"
    """<p>The URL to download the static file from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticFileUrlSourceOptions) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> StaticFileUrlSourceOptions:
    out: StaticFileUrlSourceOptions = {}  # type: ignore[typeddict-item]
    if "Url" in data:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("StaticFileUrlSourceOptions.url required")
    return out
