"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineStyleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.reference_line_pattern_type


class ReferenceLineStyleConfiguration(TypedDict, closed=True):
    pattern: NotRequired[
        "capo_quicksight.types.reference_line_pattern_type.ReferenceLinePatternType"
    ]
    """<p>The pattern type of the line style. Choose one of the following options:</p> <ul> <li> <p> <code>SOLID</code> </p> </li> <li> <p> <code>DASHED</code> </p> </li> <li> <p> <code>DOTTED</code> </p> </li> </ul>"""
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The hex color of the reference line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineStyleConfiguration) -> dict:
    out: dict = {}
    if "pattern" in value:
        import capo_quicksight.types.reference_line_pattern_type

        out["Pattern"] = (
            capo_quicksight.types.reference_line_pattern_type.serialize_json(
                value["pattern"]
            )
        )
    if "color" in value:
        out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> ReferenceLineStyleConfiguration:
    out: ReferenceLineStyleConfiguration = {}  # type: ignore[typeddict-item]
    if "Pattern" in data:
        import capo_quicksight.types.reference_line_pattern_type

        out["pattern"] = (
            capo_quicksight.types.reference_line_pattern_type.deserialize_json(
                data["Pattern"]
            )
        )
    if "Color" in data:
        out["color"] = data["Color"]
    return out
