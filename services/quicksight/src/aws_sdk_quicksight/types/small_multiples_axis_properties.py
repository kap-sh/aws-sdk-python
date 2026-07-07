"""Generated from Smithy shape ``com.amazonaws.quicksight#SmallMultiplesAxisProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.small_multiples_axis_placement
    import aws_sdk_quicksight.types.small_multiples_axis_scale


class SmallMultiplesAxisProperties(TypedDict, closed=True):
    scale: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_axis_scale.SmallMultiplesAxisScale"
    ]
    """<p>Determines whether scale of the axes are shared or independent. The default value is <code>SHARED</code>.</p>"""
    placement: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_axis_placement.SmallMultiplesAxisPlacement"
    ]
    """<p>Defines the placement of the axis. By default, axes are rendered <code>OUTSIDE</code> of the panels. Axes with <code>INDEPENDENT</code> scale are rendered <code>INSIDE</code> the panels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SmallMultiplesAxisProperties) -> dict:
    out: dict = {}
    if "scale" in value:
        import aws_sdk_quicksight.types.small_multiples_axis_scale

        out["Scale"] = (
            aws_sdk_quicksight.types.small_multiples_axis_scale.serialize_json(
                value["scale"]
            )
        )
    if "placement" in value:
        import aws_sdk_quicksight.types.small_multiples_axis_placement

        out["Placement"] = (
            aws_sdk_quicksight.types.small_multiples_axis_placement.serialize_json(
                value["placement"]
            )
        )
    return out


def deserialize_json(data: dict) -> SmallMultiplesAxisProperties:
    out: SmallMultiplesAxisProperties = {}  # type: ignore[typeddict-item]
    if "Scale" in data:
        import aws_sdk_quicksight.types.small_multiples_axis_scale

        out["scale"] = (
            aws_sdk_quicksight.types.small_multiples_axis_scale.deserialize_json(
                data["Scale"]
            )
        )
    if "Placement" in data:
        import aws_sdk_quicksight.types.small_multiples_axis_placement

        out["placement"] = (
            aws_sdk_quicksight.types.small_multiples_axis_placement.deserialize_json(
                data["Placement"]
            )
        )
    return out
