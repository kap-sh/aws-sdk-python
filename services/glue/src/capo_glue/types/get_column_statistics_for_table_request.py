"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsForTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.get_column_names_list
    import capo_glue.types.name_string


class GetColumnStatisticsForTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    column_names: "capo_glue.types.get_column_names_list.GetColumnNamesList"
    """<p>A list of the column names.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsForTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.get_column_names_list

    out["ColumnNames"] = capo_glue.types.get_column_names_list.serialize_aws_json_1_1(
        value["column_names"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsForTableRequest:
    out: GetColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsForTableRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsForTableRequest.table_name required"
        )
    if "ColumnNames" in data:
        import capo_glue.types.get_column_names_list

        out["column_names"] = (
            capo_glue.types.get_column_names_list.deserialize_aws_json_1_1(
                data["ColumnNames"]
            )
        )
    else:
        raise DeserializationError(
            "GetColumnStatisticsForTableRequest.column_names required"
        )
    return out
