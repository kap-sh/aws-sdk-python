"""Generated from Smithy shape ``com.amazonaws.quicksight#BookmarksConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean


class BookmarksConfigurations(TypedDict, closed=True):
    enabled: "capo_quicksight.types.boolean.Boolean"
    """<p>A Boolean value that determines whether a user can bookmark an embedded dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BookmarksConfigurations) -> dict:
    out: dict = {}
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> BookmarksConfigurations:
    out: BookmarksConfigurations = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
