"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.data_table_name
    import aws_sdk_connect.types.string


class PrimaryValue(TypedDict, closed=True):
    attribute_name: "aws_sdk_connect.types.data_table_name.DataTableName"
    """<p>The name of the primary attribute that this value belongs to.</p>"""
    value: "aws_sdk_connect.types.string.String"
    """<p>The actual value for the primary attribute. Must be provided as a string regardless of the attribute's value type. Primary values cannot be expressions and must be explicitly specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValue) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> PrimaryValue:
    out: PrimaryValue = {}  # type: ignore[typeddict-item]
    if "AttributeName" in data:
        out["attribute_name"] = data["AttributeName"]
    else:
        raise DeserializationError("PrimaryValue.attribute_name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("PrimaryValue.value required")
    return out
