"""Generated from Smithy shape ``com.amazonaws.datapipeline#ParameterValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_name_string
    import aws_sdk_data_pipeline.types.field_string_value


class ParameterValue(TypedDict, closed=True):
    id: "aws_sdk_data_pipeline.types.field_name_string.fieldNameString"
    """<p>The ID of the parameter value.</p>"""
    string_value: "aws_sdk_data_pipeline.types.field_string_value.fieldStringValue"
    """<p>The field value, expressed as a String.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterValue) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["stringValue"] = value["string_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParameterValue:
    out: ParameterValue = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ParameterValue.id required")
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    else:
        raise DeserializationError("ParameterValue.string_value required")
    return out
