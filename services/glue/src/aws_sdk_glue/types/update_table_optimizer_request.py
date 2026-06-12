"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTableOptimizerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.table_optimizer_configuration
    import aws_sdk_glue.types.table_optimizer_type


class UpdateTableOptimizerRequest(TypedDict):
    catalog_id: "aws_sdk_glue.types.catalog_id_string.CatalogIdString"
    """<p>The Catalog ID of the table.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the database in the catalog in which the table resides.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    type: "aws_sdk_glue.types.table_optimizer_type.TableOptimizerType"
    """<p>The type of table optimizer.</p>"""
    table_optimizer_configuration: (
        "aws_sdk_glue.types.table_optimizer_configuration.TableOptimizerConfiguration"
    )
    """<p>A <code>TableOptimizerConfiguration</code> object representing the configuration of a table optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTableOptimizerRequest) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.table_optimizer_type

    out["Type"] = aws_sdk_glue.types.table_optimizer_type.serialize_aws_json_1_1(
        value["type"]
    )
    import aws_sdk_glue.types.table_optimizer_configuration

    out["TableOptimizerConfiguration"] = (
        aws_sdk_glue.types.table_optimizer_configuration.serialize_aws_json_1_1(
            value["table_optimizer_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTableOptimizerRequest:
    out: UpdateTableOptimizerRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    else:
        raise DeserializationError("UpdateTableOptimizerRequest.catalog_id required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdateTableOptimizerRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("UpdateTableOptimizerRequest.table_name required")
    if "Type" in data:
        import aws_sdk_glue.types.table_optimizer_type

        out["type"] = aws_sdk_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("UpdateTableOptimizerRequest.type required")
    if "TableOptimizerConfiguration" in data:
        import aws_sdk_glue.types.table_optimizer_configuration

        out["table_optimizer_configuration"] = (
            aws_sdk_glue.types.table_optimizer_configuration.deserialize_aws_json_1_1(
                data["TableOptimizerConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTableOptimizerRequest.table_optimizer_configuration required"
        )
    return out
