"""Generated from Smithy shape ``com.amazonaws.quicksight#GradientColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.gradient_stop_list


class GradientColor(TypedDict, closed=True):
    stops: NotRequired["capo_quicksight.types.gradient_stop_list.GradientStopList"]
    """<p>The list of gradient color stops.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GradientColor) -> dict:
    out: dict = {}
    if "stops" in value:
        import capo_quicksight.types.gradient_stop_list

        out["Stops"] = capo_quicksight.types.gradient_stop_list.serialize_json(
            value["stops"]
        )
    return out


def deserialize_json(data: dict) -> GradientColor:
    out: GradientColor = {}  # type: ignore[typeddict-item]
    if "Stops" in data:
        import capo_quicksight.types.gradient_stop_list

        out["stops"] = capo_quicksight.types.gradient_stop_list.deserialize_json(
            data["Stops"]
        )
    return out
