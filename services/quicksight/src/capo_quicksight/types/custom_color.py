"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_value
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.special_value


class CustomColor(TypedDict, closed=True):
    field_value: NotRequired["capo_quicksight.types.field_value.FieldValue"]
    """<p>The data value that the color is applied to.</p>"""
    color: "capo_quicksight.types.hex_color.HexColor"
    """<p>The color that is applied to the data value.</p>"""
    special_value: NotRequired["capo_quicksight.types.special_value.SpecialValue"]
    """<p>The value of a special data value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomColor) -> dict:
    out: dict = {}
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    out["Color"] = value["color"]
    if "special_value" in value:
        import capo_quicksight.types.special_value

        out["SpecialValue"] = capo_quicksight.types.special_value.serialize_json(
            value["special_value"]
        )
    return out


def deserialize_json(data: dict) -> CustomColor:
    out: CustomColor = {}  # type: ignore[typeddict-item]
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    if "Color" in data:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("CustomColor.color required")
    if "SpecialValue" in data:
        import capo_quicksight.types.special_value

        out["special_value"] = capo_quicksight.types.special_value.deserialize_json(
            data["SpecialValue"]
        )
    return out
