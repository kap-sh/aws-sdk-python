"""Generated from Smithy shape ``com.amazonaws.glue#AllowedValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.allowed_value_description_string
    import aws_sdk_glue.types.allowed_value_value_string


class AllowedValue(TypedDict):
    description: NotRequired[
        "aws_sdk_glue.types.allowed_value_description_string.AllowedValueDescriptionString"
    ]
    """<p>A description of the allowed value.</p>"""
    value: "aws_sdk_glue.types.allowed_value_value_string.AllowedValueValueString"
    """<p>The value allowed for the property.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedValue) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AllowedValue:
    out: AllowedValue = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("AllowedValue.value required")
    return out
