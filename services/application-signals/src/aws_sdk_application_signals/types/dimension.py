"""Generated from Smithy shape ``com.amazonaws.applicationsignals#Dimension``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.dimension_name
    import aws_sdk_application_signals.types.dimension_value


class Dimension(TypedDict, closed=True):
    name: "aws_sdk_application_signals.types.dimension_name.DimensionName"
    """<p>The name of the dimension. Dimension names must contain only ASCII characters, must include at least one non-whitespace character, and cannot start with a colon (<code>:</code>). ASCII control characters are not supported as part of dimension names.</p>"""
    value: "aws_sdk_application_signals.types.dimension_value.DimensionValue"
    """<p>The value of the dimension. Dimension values must contain only ASCII characters and must include at least one non-whitespace character. ASCII control characters are not supported as part of dimension values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> Dimension:
    out: Dimension = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Dimension.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("Dimension.value required")
    return out
