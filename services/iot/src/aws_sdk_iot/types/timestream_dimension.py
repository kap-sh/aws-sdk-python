"""Generated from Smithy shape ``com.amazonaws.iot#TimestreamDimension``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.timestream_dimension_name
    import aws_sdk_iot.types.timestream_dimension_value


class TimestreamDimension(TypedDict):
    name: "aws_sdk_iot.types.timestream_dimension_name.TimestreamDimensionName"
    """<p>The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.</p> <p>Dimensions cannot be named: <code>measure_name</code>, <code>measure_value</code>, or <code>time</code>. These names are reserved. Dimension names cannot start with <code>ts_</code> or <code>measure_value</code> and they cannot contain the colon (<code>:</code>) character.</p>"""
    value: "aws_sdk_iot.types.timestream_dimension_value.TimestreamDimensionValue"
    """<p>The value to write in this column of the database record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimestreamDimension) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TimestreamDimension:
    out: TimestreamDimension = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TimestreamDimension.name required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TimestreamDimension.value required")
    return out
