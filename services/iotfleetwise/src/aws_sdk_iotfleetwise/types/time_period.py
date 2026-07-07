"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.positive_integer
    import aws_sdk_iotfleetwise.types.time_unit


class TimePeriod(TypedDict, closed=True):
    unit: "aws_sdk_iotfleetwise.types.time_unit.TimeUnit"
    """<p>A unit of time.</p>"""
    value: "aws_sdk_iotfleetwise.types.positive_integer.positiveInteger"
    """<p>A number of time units.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriod) -> dict:
    out: dict = {}
    import aws_sdk_iotfleetwise.types.time_unit

    out["unit"] = aws_sdk_iotfleetwise.types.time_unit.serialize_aws_json_1_0(
        value["unit"]
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if "unit" in data:
        import aws_sdk_iotfleetwise.types.time_unit

        out["unit"] = aws_sdk_iotfleetwise.types.time_unit.deserialize_aws_json_1_0(
            data["unit"]
        )
    else:
        raise DeserializationError("TimePeriod.unit required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TimePeriod.value required")
    return out
