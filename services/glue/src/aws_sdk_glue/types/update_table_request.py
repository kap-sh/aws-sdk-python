"""Generated from Smithy shape ``com.amazonaws.glue#UpdateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.boolean
    import aws_sdk_glue.types.boolean_nullable
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.table_input
    import aws_sdk_glue.types.transaction_id_string
    import aws_sdk_glue.types.update_open_table_format_input
    import aws_sdk_glue.types.version_string
    import aws_sdk_glue.types.view_update_action


class UpdateTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the table resides. If none is provided, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database in which the table resides. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The unique identifier for the table within the specified database that will be created in the Glue Data Catalog.</p>"""
    table_input: NotRequired["aws_sdk_glue.types.table_input.TableInput"]
    """<p>An updated <code>TableInput</code> object to define the metadata table in the catalog.</p>"""
    skip_archive: NotRequired["aws_sdk_glue.types.boolean_nullable.BooleanNullable"]
    """<p>By default, <code>UpdateTable</code> always creates an archived version of the table before updating it. However, if <code>skipArchive</code> is set to true, <code>UpdateTable</code> does not create the archived version.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The transaction ID at which to update the table contents. </p>"""
    version_id: NotRequired["aws_sdk_glue.types.version_string.VersionString"]
    """<p>The version ID at which to update the table contents. </p>"""
    view_update_action: NotRequired[
        "aws_sdk_glue.types.view_update_action.ViewUpdateAction"
    ]
    """<p>The operation to be performed when updating the view.</p>"""
    force: "aws_sdk_glue.types.boolean.Boolean"
    """<p>A flag that can be set to true to ignore matching storage descriptor and subobject matching requirements.</p>"""
    update_open_table_format_input: NotRequired[
        "aws_sdk_glue.types.update_open_table_format_input.UpdateOpenTableFormatInput"
    ]
    """<p>Input parameters for updating open table format tables in GlueData Catalog, serving as a wrapper for format-specific update operations such as Apache Iceberg.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "table_input" in value:
        import aws_sdk_glue.types.table_input

        out["TableInput"] = aws_sdk_glue.types.table_input.serialize_aws_json_1_1(
            value["table_input"]
        )
    if "skip_archive" in value:
        out["SkipArchive"] = value["skip_archive"]
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "view_update_action" in value:
        import aws_sdk_glue.types.view_update_action

        out["ViewUpdateAction"] = (
            aws_sdk_glue.types.view_update_action.serialize_aws_json_1_1(
                value["view_update_action"]
            )
        )
    out["Force"] = value.get("force", False)
    if "update_open_table_format_input" in value:
        import aws_sdk_glue.types.update_open_table_format_input

        out["UpdateOpenTableFormatInput"] = (
            aws_sdk_glue.types.update_open_table_format_input.serialize_aws_json_1_1(
                value["update_open_table_format_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTableRequest:
    out: UpdateTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("UpdateTableRequest.database_name required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "TableInput" in data:
        import aws_sdk_glue.types.table_input

        out["table_input"] = aws_sdk_glue.types.table_input.deserialize_aws_json_1_1(
            data["TableInput"]
        )
    if "SkipArchive" in data:
        out["skip_archive"] = data["SkipArchive"]
    if "TransactionId" in data:
        out["transaction_id"] = data["TransactionId"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "ViewUpdateAction" in data:
        import aws_sdk_glue.types.view_update_action

        out["view_update_action"] = (
            aws_sdk_glue.types.view_update_action.deserialize_aws_json_1_1(
                data["ViewUpdateAction"]
            )
        )
    if "Force" in data:
        out["force"] = data["Force"]
    else:
        out["force"] = False
    if "UpdateOpenTableFormatInput" in data:
        import aws_sdk_glue.types.update_open_table_format_input

        out["update_open_table_format_input"] = (
            aws_sdk_glue.types.update_open_table_format_input.deserialize_aws_json_1_1(
                data["UpdateOpenTableFormatInput"]
            )
        )
    return out
