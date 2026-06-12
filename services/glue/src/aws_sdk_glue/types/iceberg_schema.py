"""Generated from Smithy shape ``com.amazonaws.glue#IcebergSchema``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_struct_field_list
    import aws_sdk_glue.types.iceberg_struct_type_enum
    import aws_sdk_glue.types.integer
    import aws_sdk_glue.types.integer_list


class IcebergSchema(TypedDict):
    schema_id: "aws_sdk_glue.types.integer.Integer"
    """<p>The unique identifier for this schema version within the Iceberg table's schema evolution history.</p>"""
    identifier_field_ids: NotRequired["aws_sdk_glue.types.integer_list.IntegerList"]
    """<p>The list of field identifiers that uniquely identify records in the table, used for row-level operations and deduplication.</p>"""
    type: NotRequired[
        "aws_sdk_glue.types.iceberg_struct_type_enum.IcebergStructTypeEnum"
    ]
    """<p>The root type of the schema structure, typically \"struct\" for Iceberg table schemas.</p>"""
    fields: "aws_sdk_glue.types.iceberg_struct_field_list.IcebergStructFieldList"
    """<p>The list of field definitions that make up the table schema, including field names, types, and metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergSchema) -> dict:
    out: dict = {}
    out["SchemaId"] = value.get("schema_id", 0)
    if "identifier_field_ids" in value:
        import aws_sdk_glue.types.integer_list

        out["IdentifierFieldIds"] = (
            aws_sdk_glue.types.integer_list.serialize_aws_json_1_1(
                value["identifier_field_ids"]
            )
        )
    if "type" in value:
        import aws_sdk_glue.types.iceberg_struct_type_enum

        out["Type"] = (
            aws_sdk_glue.types.iceberg_struct_type_enum.serialize_aws_json_1_1(
                value["type"]
            )
        )
    import aws_sdk_glue.types.iceberg_struct_field_list

    out["Fields"] = aws_sdk_glue.types.iceberg_struct_field_list.serialize_aws_json_1_1(
        value["fields"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergSchema:
    out: IcebergSchema = {}  # type: ignore[typeddict-item]
    if "SchemaId" in data:
        out["schema_id"] = data["SchemaId"]
    else:
        out["schema_id"] = 0
    if "IdentifierFieldIds" in data:
        import aws_sdk_glue.types.integer_list

        out["identifier_field_ids"] = (
            aws_sdk_glue.types.integer_list.deserialize_aws_json_1_1(
                data["IdentifierFieldIds"]
            )
        )
    if "Type" in data:
        import aws_sdk_glue.types.iceberg_struct_type_enum

        out["type"] = (
            aws_sdk_glue.types.iceberg_struct_type_enum.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Fields" in data:
        import aws_sdk_glue.types.iceberg_struct_field_list

        out["fields"] = (
            aws_sdk_glue.types.iceberg_struct_field_list.deserialize_aws_json_1_1(
                data["Fields"]
            )
        )
    else:
        raise DeserializationError("IcebergSchema.fields required")
    return out
