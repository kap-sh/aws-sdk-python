"""Generated from Smithy shape ``com.amazonaws.quicksight#Entity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.non_empty_string


class Entity(TypedDict, closed=True):
    path: NotRequired["capo_quicksight.types.non_empty_string.NonEmptyString"]
    """<p>The hierarchical path of the entity within the analysis, template, or dashboard definition tree.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Entity) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "Path" in data:
        out["path"] = data["Path"]
    return out
