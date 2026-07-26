"""Generated from Smithy shape ``com.amazonaws.quicksight#ListControlSelectAllOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class ListControlSelectAllOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility configuration of the <code>Select all</code> options in a list control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlSelectAllOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    return out


def deserialize_json(data: dict) -> ListControlSelectAllOptions:
    out: ListControlSelectAllOptions = {}  # type: ignore[typeddict-item]
    if "Visibility" in data:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    return out
