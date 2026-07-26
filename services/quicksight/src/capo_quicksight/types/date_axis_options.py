"""Generated from Smithy shape ``com.amazonaws.quicksight#DateAxisOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class DateAxisOptions(TypedDict, closed=True):
    missing_date_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines whether or not missing dates are displayed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateAxisOptions) -> dict:
    out: dict = {}
    if "missing_date_visibility" in value:
        import capo_quicksight.types.visibility

        out["MissingDateVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["missing_date_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DateAxisOptions:
    out: DateAxisOptions = {}  # type: ignore[typeddict-item]
    if "MissingDateVisibility" in data:
        import capo_quicksight.types.visibility

        out["missing_date_visibility"] = (
            capo_quicksight.types.visibility.deserialize_json(
                data["MissingDateVisibility"]
            )
        )
    return out
