"""Generated from Smithy shape ``com.amazonaws.glue#FieldDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.field_data_type


class FieldDefinition(TypedDict, closed=True):
    name: "str"
    """<p>The name of the field in the entity schema.</p>"""
    field_data_type: "aws_sdk_glue.types.field_data_type.FieldDataType"
    """<p>The data type of the field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldDefinition) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.field_data_type

    out["FieldDataType"] = aws_sdk_glue.types.field_data_type.serialize_aws_json_1_1(
        value["field_data_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldDefinition:
    out: FieldDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FieldDefinition.name required")
    if "FieldDataType" in data:
        import aws_sdk_glue.types.field_data_type

        out["field_data_type"] = (
            aws_sdk_glue.types.field_data_type.deserialize_aws_json_1_1(
                data["FieldDataType"]
            )
        )
    else:
        raise DeserializationError("FieldDefinition.field_data_type required")
    return out
