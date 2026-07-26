"""Generated from Smithy shape ``com.amazonaws.quicksight#GradientStopList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.gradient_stop

GradientStopList: TypeAlias = list["capo_quicksight.types.gradient_stop.GradientStop"]


# --- restJson1 ser/de ---
def serialize_json(value: GradientStopList) -> list:
    import capo_quicksight.types.gradient_stop

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.gradient_stop.serialize_json(item))
    return out


def deserialize_json(data: list) -> GradientStopList:
    import capo_quicksight.types.gradient_stop

    out: GradientStopList = []
    for item in data:
        out.append(capo_quicksight.types.gradient_stop.deserialize_json(item))
    return out
