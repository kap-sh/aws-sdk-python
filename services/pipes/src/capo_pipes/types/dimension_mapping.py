"""Generated from Smithy shape ``com.amazonaws.pipes#DimensionMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pipes.types.dimension_name
    import capo_pipes.types.dimension_value
    import capo_pipes.types.dimension_value_type


class DimensionMapping(TypedDict, closed=True):
    dimension_value: "capo_pipes.types.dimension_value.DimensionValue"
    """<p>Dynamic path to the dimension value in the source event.</p>"""
    dimension_value_type: "capo_pipes.types.dimension_value_type.DimensionValueType"
    """<p>The data type of the dimension for the time-series data.</p>"""
    dimension_name: "capo_pipes.types.dimension_name.DimensionName"
    """<p>The metadata attributes of the time series. For example, the name and Availability Zone of an Amazon EC2 instance or the name of the manufacturer of a wind turbine are dimensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DimensionMapping) -> dict:
    out: dict = {}
    out["DimensionValue"] = value["dimension_value"]
    out["DimensionValueType"] = value["dimension_value_type"]
    out["DimensionName"] = value["dimension_name"]
    return out


def deserialize_json(data: dict) -> DimensionMapping:
    out: DimensionMapping = {}  # type: ignore[typeddict-item]
    if "DimensionValue" in data:
        out["dimension_value"] = data["DimensionValue"]
    else:
        raise DeserializationError("DimensionMapping.dimension_value required")
    if "DimensionValueType" in data:
        out["dimension_value_type"] = data["DimensionValueType"]
    else:
        raise DeserializationError("DimensionMapping.dimension_value_type required")
    if "DimensionName" in data:
        out["dimension_name"] = data["DimensionName"]
    else:
        raise DeserializationError("DimensionMapping.dimension_name required")
    return out
