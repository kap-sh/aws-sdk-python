"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#PropertyValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iottwinmaker.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.time
    import aws_sdk_iottwinmaker.types.timestamp


class PropertyValue(TypedDict, closed=True):
    timestamp: NotRequired["aws_sdk_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The timestamp of a value for a time series property.</p>"""
    value: "aws_sdk_iottwinmaker.types.data_value.DataValue"
    """<p>An object that specifies a value for a time series property.</p>"""
    time: NotRequired["aws_sdk_iottwinmaker.types.time.Time"]
    """<p>ISO8601 DateTime of a value for a time series property.</p> <p>The time for when the property value was recorded in ISO 8601 format: <i>YYYY-MM-DDThh:mm:ss[.SSSSSSSSS][Z/±HH:mm]</i>.</p> <ul> <li> <p> <i>[YYYY]</i>: year</p> </li> <li> <p> <i>[MM]</i>: month</p> </li> <li> <p> <i>[DD]</i>: day</p> </li> <li> <p> <i>[hh]</i>: hour</p> </li> <li> <p> <i>[mm]</i>: minute</p> </li> <li> <p> <i>[ss]</i>: seconds</p> </li> <li> <p> <i>[.SSSSSSSSS]</i>: additional precision, where precedence is maintained. For example: [.573123] is equal to 573123000 nanoseconds.</p> </li> <li> <p> <i>Z</i>: default timezone UTC</p> </li> <li> <p> <i>± HH:mm</i>: time zone offset in Hours and Minutes.</p> </li> </ul> <p> <i>Required sub-fields</i>: YYYY-MM-DDThh:mm:ss and [Z/±HH:mm]</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValue) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import aws_sdk_iottwinmaker.types.timestamp

        out["timestamp"] = aws_sdk_iottwinmaker.types.timestamp.serialize_json(
            value["timestamp"]
        )
    import aws_sdk_iottwinmaker.types.data_value

    out["value"] = aws_sdk_iottwinmaker.types.data_value.serialize_json(value["value"])
    if "time" in value:
        out["time"] = value["time"]
    return out


def deserialize_json(data: dict) -> PropertyValue:
    out: PropertyValue = {}  # type: ignore[typeddict-item]
    if "timestamp" in data:
        import aws_sdk_iottwinmaker.types.timestamp

        out["timestamp"] = aws_sdk_iottwinmaker.types.timestamp.deserialize_json(
            data["timestamp"]
        )
    if "value" in data:
        import aws_sdk_iottwinmaker.types.data_value

        out["value"] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(
            data["value"]
        )
    else:
        raise DeserializationError("PropertyValue.value required")
    if "time" in data:
        out["time"] = data["time"]
    return out
