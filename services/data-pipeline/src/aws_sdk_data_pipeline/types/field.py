"""Generated from Smithy shape ``com.amazonaws.datapipeline#Field``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.field_name_string
    import aws_sdk_data_pipeline.types.field_string_value


class Field(TypedDict, closed=True):
    key: "aws_sdk_data_pipeline.types.field_name_string.fieldNameString"
    """<p>The field identifier.</p>"""
    string_value: NotRequired[
        "aws_sdk_data_pipeline.types.field_string_value.fieldStringValue"
    ]
    """<p>The field value, expressed as a String.</p>"""
    ref_value: NotRequired[
        "aws_sdk_data_pipeline.types.field_name_string.fieldNameString"
    ]
    """<p>The field value, expressed as the identifier of another object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Field) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "ref_value" in value:
        out["refValue"] = value["ref_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Field:
    out: Field = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("Field.key required")
    if "stringValue" in data:
        out["string_value"] = data["stringValue"]
    if "refValue" in data:
        out["ref_value"] = data["refValue"]
    return out
