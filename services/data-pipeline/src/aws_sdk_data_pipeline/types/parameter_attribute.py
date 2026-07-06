"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.attribute_name_string
    import aws_sdk_data_pipeline.types.attribute_value_string


class ParameterAttribute(TypedDict, closed=True):
    key: "aws_sdk_data_pipeline.types.attribute_name_string.attributeNameString"
    """<p>The field identifier.</p>"""
    string_value: (
        "aws_sdk_data_pipeline.types.attribute_value_string.attributeValueString"
    )
    """<p>The field value, expressed as a String.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    out["stringValue"] = value["string_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterAttribute:
    out: ParameterAttribute = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ParameterAttribute.key required")
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    else:
        raise DeserializationError("ParameterAttribute.string_value required")
    return out
