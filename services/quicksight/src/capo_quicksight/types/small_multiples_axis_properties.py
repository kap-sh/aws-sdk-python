"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.small_multiples_axis_placement
    import capo_quicksight.types.small_multiples_axis_scale


class SmallMultiplesAxisProperties(TypedDict, closed=True):
    scale: NotRequired[
        "capo_quicksight.types.small_multiples_axis_scale.SmallMultiplesAxisScale"
    ]
    """<p>Determines whether scale of the axes are shared or independent. The default value is <code>SHARED</code>.</p>"""
    placement: NotRequired[
        "capo_quicksight.types.small_multiples_axis_placement.SmallMultiplesAxisPlacement"
    ]
    """<p>Defines the placement of the axis. By default, axes are rendered <code>OUTSIDE</code> of the panels. Axes with <code>INDEPENDENT</code> scale are rendered <code>INSIDE</code> the panels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SmallMultiplesAxisProperties) -> dict:
    out: dict = {}
    if "scale" in value:
        import capo_quicksight.types.small_multiples_axis_scale

        out["Scale"] = capo_quicksight.types.small_multiples_axis_scale.serialize_json(
            value["scale"]
        )
    if "placement" in value:
        import capo_quicksight.types.small_multiples_axis_placement

        out["Placement"] = (
            capo_quicksight.types.small_multiples_axis_placement.serialize_json(
                value["placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> SmallMultiplesAxisProperties:
    out: SmallMultiplesAxisProperties = {}  # type: ignore[typeddict-item]
    if "Scale" in data:
        import capo_quicksight.types.small_multiples_axis_scale

        out["scale"] = (
            capo_quicksight.types.small_multiples_axis_scale.deserialize_json(
                data["Scale"]
            )
        )
    if "Placement" in data:
        import capo_quicksight.types.small_multiples_axis_placement

        out["placement"] = (
            capo_quicksight.types.small_multiples_axis_placement.deserialize_json(
                data["Placement"]
            )
        )
    return out
