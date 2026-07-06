"""Generated from Smithy shape ``com.amazonaws.glue#CatalogIcebergSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.additional_options
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name


class CatalogIcebergSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the Iceberg data source.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    additional_iceberg_options: NotRequired[
        "aws_sdk_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options for the Iceberg data source.</p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the Iceberg source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogIcebergSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "additional_iceberg_options" in value:
        import aws_sdk_glue.types.additional_options

        out["AdditionalIcebergOptions"] = (
            aws_sdk_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_iceberg_options"]
            )
        )
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogIcebergSource:
    out: CatalogIcebergSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CatalogIcebergSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("CatalogIcebergSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("CatalogIcebergSource.table required")
    if "AdditionalIcebergOptions" in data:
        import aws_sdk_glue.types.additional_options

        out["additional_iceberg_options"] = (
            aws_sdk_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalIcebergOptions"]
            )
        )
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
