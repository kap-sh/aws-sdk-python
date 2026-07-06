"""Generated from Smithy shape ``com.amazonaws.glue#CatalogSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_schemas
    import aws_sdk_glue.types.node_name


class CatalogSource(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data store.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to read from.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to read from.</p>"""
    partition_predicate: NotRequired[
        "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p> Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted. </p>"""
    output_schemas: NotRequired["aws_sdk_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the catalog source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CatalogSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Database"] = value["database"]
    out["Table"] = value["table"]
    if "partition_predicate" in value:
        out["PartitionPredicate"] = value["partition_predicate"]
    if "output_schemas" in value:
        import aws_sdk_glue.types.glue_schemas

        out["OutputSchemas"] = aws_sdk_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CatalogSource:
    out: CatalogSource = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CatalogSource.name required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("CatalogSource.database required")
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("CatalogSource.table required")
    if "PartitionPredicate" in data:
        out["partition_predicate"] = data["PartitionPredicate"]
    if "OutputSchemas" in data:
        import aws_sdk_glue.types.glue_schemas

        out["output_schemas"] = (
            aws_sdk_glue.types.glue_schemas.deserialize_aws_json_1_1(
                data["OutputSchemas"]
            )
        )
    return out
