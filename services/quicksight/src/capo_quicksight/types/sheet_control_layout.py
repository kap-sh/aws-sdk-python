"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlLayout``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_control_layout_configuration


class SheetControlLayout(TypedDict, closed=True):
    configuration: "capo_quicksight.types.sheet_control_layout_configuration.SheetControlLayoutConfiguration"
    """<p>The configuration that determines the elements and canvas size options of sheet control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlLayout) -> dict:
    out: dict = {}
    import capo_quicksight.types.sheet_control_layout_configuration

    out["Configuration"] = (
        capo_quicksight.types.sheet_control_layout_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> SheetControlLayout:
    out: SheetControlLayout = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import capo_quicksight.types.sheet_control_layout_configuration

        out["configuration"] = (
            capo_quicksight.types.sheet_control_layout_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError("SheetControlLayout.configuration required")
    return out
