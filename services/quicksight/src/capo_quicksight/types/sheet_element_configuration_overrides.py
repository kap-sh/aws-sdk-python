"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetElementConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class SheetElementConfigurationOverrides(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not the overrides are visible. Choose one of the following options:</p> <ul> <li> <p> <code>VISIBLE</code> </p> </li> <li> <p> <code>HIDDEN</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetElementConfigurationOverrides) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> SheetElementConfigurationOverrides:
    out: SheetElementConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
