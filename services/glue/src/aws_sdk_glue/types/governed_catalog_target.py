"""Generated from Smithy shape ``com.amazonaws.glue#GovernedCatalogTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_schema_change_policy
    import aws_sdk_glue.types.enclosed_in_string_property
    import aws_sdk_glue.types.glue_studio_path_list
    import aws_sdk_glue.types.node_name
    import aws_sdk_glue.types.one_input


class GovernedCatalogTarget(TypedDict, closed=True):
    name: "aws_sdk_glue.types.node_name.NodeName"
    """<p>The name of the data target.</p>"""
    inputs: "aws_sdk_glue.types.one_input.OneInput"
    """<p>The nodes that are inputs to the data target.</p>"""
    partition_keys: NotRequired[
        "aws_sdk_glue.types.glue_studio_path_list.GlueStudioPathList"
    ]
    """<p>Specifies native partitioning using a sequence of keys.</p>"""
    table: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the table in the database to write to.</p>"""
    database: "aws_sdk_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    """<p>The name of the database to write to.</p>"""
    schema_change_policy: NotRequired[
        "aws_sdk_glue.types.catalog_schema_change_policy.CatalogSchemaChangePolicy"
    ]
    """<p>A policy that specifies update behavior for the governed catalog.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GovernedCatalogTarget) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_glue.types.one_input

    out["Inputs"] = aws_sdk_glue.types.one_input.serialize_aws_json_1_1(value["inputs"])
    if "partition_keys" in value:
        import aws_sdk_glue.types.glue_studio_path_list

        out["PartitionKeys"] = (
            aws_sdk_glue.types.glue_studio_path_list.serialize_aws_json_1_1(
                value["partition_keys"]
            )
        )
    out["Table"] = value["table"]
    out["Database"] = value["database"]
    if "schema_change_policy" in value:
        import aws_sdk_glue.types.catalog_schema_change_policy

        out["SchemaChangePolicy"] = (
            aws_sdk_glue.types.catalog_schema_change_policy.serialize_aws_json_1_1(
                value["schema_change_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GovernedCatalogTarget:
    out: GovernedCatalogTarget = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GovernedCatalogTarget.name required")
    if "Inputs" in data:
        import aws_sdk_glue.types.one_input

        out["inputs"] = aws_sdk_glue.types.one_input.deserialize_aws_json_1_1(
            data["Inputs"]
        )
    else:
        raise DeserializationError("GovernedCatalogTarget.inputs required")
    if "PartitionKeys" in data:
        import aws_sdk_glue.types.glue_studio_path_list

        out["partition_keys"] = (
            aws_sdk_glue.types.glue_studio_path_list.deserialize_aws_json_1_1(
                data["PartitionKeys"]
            )
        )
    if "Table" in data:
        out["table"] = data["Table"]
    else:
        raise DeserializationError("GovernedCatalogTarget.table required")
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("GovernedCatalogTarget.database required")
    if "SchemaChangePolicy" in data:
        import aws_sdk_glue.types.catalog_schema_change_policy

        out["schema_change_policy"] = (
            aws_sdk_glue.types.catalog_schema_change_policy.deserialize_aws_json_1_1(
                data["SchemaChangePolicy"]
            )
        )
    return out
