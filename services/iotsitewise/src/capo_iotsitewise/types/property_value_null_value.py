"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyValueNullValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.raw_value_type


class PropertyValueNullValue(TypedDict, closed=True):
    value_type: "capo_iotsitewise.types.raw_value_type.RawValueType"
    """<p>The type of null asset property data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyValueNullValue) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.raw_value_type

    out["valueType"] = capo_iotsitewise.types.raw_value_type.serialize_json(
        value["value_type"]
    )
    return out


def deserialize_json(data: dict) -> PropertyValueNullValue:
    out: PropertyValueNullValue = {}  # type: ignore[typeddict-item]
    if "valueType" in data:
        import capo_iotsitewise.types.raw_value_type

        out["value_type"] = capo_iotsitewise.types.raw_value_type.deserialize_json(
            data["valueType"]
        )
    else:
        raise DeserializationError("PropertyValueNullValue.value_type required")
    return out
