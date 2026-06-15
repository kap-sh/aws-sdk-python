"""Generated from Smithy shape ``com.amazonaws.iot#UpdateDimensionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.dimension_name
    import aws_sdk_iot.types.dimension_string_values


class UpdateDimensionRequest(TypedDict):
    name: "aws_sdk_iot.types.dimension_name.DimensionName"
    """<p>A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.</p>"""
    string_values: "aws_sdk_iot.types.dimension_string_values.DimensionStringValues"
    r"""<p>Specifies the value or list of values for the dimension. For <code>TOPIC_FILTER</code> dimensions, this is a pattern used to match the MQTT topic (for example, \"admin/#\").</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDimensionRequest) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.dimension_string_values

    out["stringValues"] = aws_sdk_iot.types.dimension_string_values.serialize_json(
        value["string_values"]
    )
    return out


def deserialize_json(data: dict) -> UpdateDimensionRequest:
    out: UpdateDimensionRequest = {}  # type: ignore[typeddict-item]
    if "stringValues" in data:
        import aws_sdk_iot.types.dimension_string_values

        out["string_values"] = (
            aws_sdk_iot.types.dimension_string_values.deserialize_json(
                data["stringValues"]
            )
        )
    else:
        raise DeserializationError("UpdateDimensionRequest.string_values required")
    return out
