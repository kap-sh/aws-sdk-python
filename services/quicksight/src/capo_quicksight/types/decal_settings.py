"""Generated from Smithy shape ``com.amazonaws.quicksight#DecalSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.decal_pattern_type
    import capo_quicksight.types.decal_style_type
    import capo_quicksight.types.element_value
    import capo_quicksight.types.hex_color_with_transparency
    import capo_quicksight.types.visibility


class DecalSettings(TypedDict, closed=True):
    element_value: NotRequired["capo_quicksight.types.element_value.ElementValue"]
    """<p>Field value of the field that you are setting the decal pattern to. Applicable only for field level settings.</p>"""
    decal_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>Visibility setting for the decal pattern.</p>"""
    decal_color: NotRequired[
        "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    ]
    """<p>Color configuration for the decal pattern.</p>"""
    decal_pattern_type: NotRequired[
        "capo_quicksight.types.decal_pattern_type.DecalPatternType"
    ]
    """<p>Type of pattern used for the decal, such as solid, diagonal, or circular patterns in various sizes.</p> <ul> <li> <p> <code>SOLID</code>: Solid fill pattern.</p> </li> <li> <p> <code>DIAGONAL_SMALL</code>: Small diagonal stripes pattern.</p> </li> <li> <p> <code>DIAGONAL_MEDIUM</code>: Medium diagonal stripes pattern.</p> </li> <li> <p> <code>DIAGONAL_LARGE</code>: Large diagonal stripes pattern.</p> </li> <li> <p> <code>DIAGONAL_OPPOSITE_SMALL</code>: Small cross-diagonal stripes pattern.</p> </li> <li> <p> <code>DIAGONAL_OPPOSITE_MEDIUM</code>: Medium cross-diagonal stripes pattern.</p> </li> <li> <p> <code>DIAGONAL_OPPOSITE_LARGE</code>: Large cross-diagonal stripes pattern.</p> </li> <li> <p> <code>CIRCLE_SMALL</code>: Small circle pattern.</p> </li> <li> <p> <code>CIRCLE_MEDIUM</code>: Medium circle pattern.</p> </li> <li> <p> <code>CIRCLE_LARGE</code>: Large circle pattern.</p> </li> <li> <p> <code>DIAMOND_SMALL</code>: Small diamonds pattern.</p> </li> <li> <p> <code>DIAMOND_MEDIUM</code>: Medium diamonds pattern.</p> </li> <li> <p> <code>DIAMOND_LARGE</code>: Large diamonds pattern.</p> </li> <li> <p> <code>DIAMOND_GRID_SMALL</code>: Small diamond grid pattern.</p> </li> <li> <p> <code>DIAMOND_GRID_MEDIUM</code>: Medium diamond grid pattern.</p> </li> <li> <p> <code>DIAMOND_GRID_LARGE</code>: Large diamond grid pattern.</p> </li> <li> <p> <code>CHECKERBOARD_SMALL</code>: Small checkerboard pattern.</p> </li> <li> <p> <code>CHECKERBOARD_MEDIUM</code>: Medium checkerboard pattern.</p> </li> <li> <p> <code>CHECKERBOARD_LARGE</code>: Large checkerboard pattern.</p> </li> <li> <p> <code>TRIANGLE_SMALL</code>: Small triangles pattern.</p> </li> <li> <p> <code>TRIANGLE_MEDIUM</code>: Medium triangles pattern.</p> </li> <li> <p> <code>TRIANGLE_LARGE</code>: Large triangles pattern.</p> </li> </ul>"""
    decal_style_type: NotRequired[
        "capo_quicksight.types.decal_style_type.DecalStyleType"
    ]
    """<p>Style type for the decal, which can be either manual or automatic. This field is only applicable for line series.</p> <ul> <li> <p> <code>Manual</code>: Apply manual line and marker configuration for line series.</p> </li> <li> <p> <code>Auto</code>: Apply automatic line and marker configuration for line series.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DecalSettings) -> dict:
    out: dict = {}
    if "element_value" in value:
        out["ElementValue"] = value["element_value"]
    if "decal_visibility" in value:
        import capo_quicksight.types.visibility

        out["DecalVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["decal_visibility"]
        )
    if "decal_color" in value:
        out["DecalColor"] = value["decal_color"]
    if "decal_pattern_type" in value:
        import capo_quicksight.types.decal_pattern_type

        out["DecalPatternType"] = (
            capo_quicksight.types.decal_pattern_type.serialize_json(
                value["decal_pattern_type"]
            )
        )
    if "decal_style_type" in value:
        import capo_quicksight.types.decal_style_type

        out["DecalStyleType"] = capo_quicksight.types.decal_style_type.serialize_json(
            value["decal_style_type"]
        )
    return out


def deserialize_json(data: dict) -> DecalSettings:
    out: DecalSettings = {}  # type: ignore[typeddict-item]
    if "ElementValue" in data:
        out["element_value"] = data["ElementValue"]
    if "DecalVisibility" in data:
        import capo_quicksight.types.visibility

        out["decal_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["DecalVisibility"]
        )
    if "DecalColor" in data:
        out["decal_color"] = data["DecalColor"]
    if "DecalPatternType" in data:
        import capo_quicksight.types.decal_pattern_type

        out["decal_pattern_type"] = (
            capo_quicksight.types.decal_pattern_type.deserialize_json(
                data["DecalPatternType"]
            )
        )
    if "DecalStyleType" in data:
        import capo_quicksight.types.decal_style_type

        out["decal_style_type"] = (
            capo_quicksight.types.decal_style_type.deserialize_json(
                data["DecalStyleType"]
            )
        )
    return out
