"""Generated from Smithy shape ``com.amazonaws.glue#UpdateColumnStatisticsForTableRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.catalog_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.update_column_statistics_list


class UpdateColumnStatisticsForTableRequest(TypedDict):
    catalog_id: NotRequired["aws_sdk_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    column_statistics_list: (
        "aws_sdk_glue.types.update_column_statistics_list.UpdateColumnStatisticsList"
    )
    """<p>A list of the column statistics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateColumnStatisticsForTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import aws_sdk_glue.types.update_column_statistics_list

    out["ColumnStatisticsList"] = (
        aws_sdk_glue.types.update_column_statistics_list.serialize_aws_json_1_1(
            value["column_statistics_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateColumnStatisticsForTableRequest:
    out: UpdateColumnStatisticsForTableRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "UpdateColumnStatisticsForTableRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "UpdateColumnStatisticsForTableRequest.table_name required"
        )
    if "ColumnStatisticsList" in data:
        import aws_sdk_glue.types.update_column_statistics_list

        out["column_statistics_list"] = (
            aws_sdk_glue.types.update_column_statistics_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsList"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateColumnStatisticsForTableRequest.column_statistics_list required"
        )
    return out
