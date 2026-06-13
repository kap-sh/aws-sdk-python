"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSchema``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.schema_field_list


class IcebergSchema(TypedDict):
    fields: "aws_sdk_s3tables.types.schema_field_list.SchemaFieldList"
    """<p>The schema fields for the table</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergSchema) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.schema_field_list

    out["fields"] = aws_sdk_s3tables.types.schema_field_list.serialize_json(
        value["fields"]
    )
    return out


def deserialize_json(data: dict) -> IcebergSchema:
    out: IcebergSchema = {}  # type: ignore[typeddict-item]
    if "fields" in data:
        import aws_sdk_s3tables.types.schema_field_list

        out["fields"] = aws_sdk_s3tables.types.schema_field_list.deserialize_json(
            data["fields"]
        )
    else:
        raise DeserializationError("IcebergSchema.fields required")
    return out
