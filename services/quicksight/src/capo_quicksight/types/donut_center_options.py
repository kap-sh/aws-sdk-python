"""Generated from Smithy shape ``com.amazonaws.quicksight#DonutCenterOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.visibility


class DonutCenterOptions(TypedDict, closed=True):
    label_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Determines the visibility of the label in a donut chart. In the Quick Sight console, this option is called <code>'Show total'</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DonutCenterOptions) -> dict:
    out: dict = {}
    if "label_visibility" in value:
        import capo_quicksight.types.visibility

        out["LabelVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["label_visibility"]
        )
    return out


def deserialize_json(data: dict) -> DonutCenterOptions:
    out: DonutCenterOptions = {}  # type: ignore[typeddict-item]
    if "LabelVisibility" in data:
        import capo_quicksight.types.visibility

        out["label_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["LabelVisibility"]
        )
    return out
