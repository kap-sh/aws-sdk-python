"""Generated from Smithy shape ``com.amazonaws.iotwireless#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.dimension_name
    import capo_iot_wireless.types.dimension_value


class Dimension(TypedDict, closed=True):
    name: NotRequired["capo_iot_wireless.types.dimension_name.DimensionName"]
    """<p>The name of the dimension.</p>"""
    value: NotRequired["capo_iot_wireless.types.dimension_value.DimensionValue"]
    """<p>The dimension's value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_iot_wireless.types.dimension_name

        out["name"] = capo_iot_wireless.types.dimension_name.serialize_json(
            value["name"]
        )
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if "name" in data:
        import capo_iot_wireless.types.dimension_name

        out["name"] = capo_iot_wireless.types.dimension_name.deserialize_json(
            data["name"]
        )
    if "value" in data:
        out["value"] = data["value"]
    return out
