"""Generated from Smithy shape ``com.amazonaws.glue#DeleteColumnStatisticsForPartitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.value_string_list


class DeleteColumnStatisticsForPartitionRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog where the partitions in question reside. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the catalog database where the partitions reside.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the partitions' table.</p>"""
    partition_values: "capo_glue.types.value_string_list.ValueStringList"
    """<p>A list of partition values identifying the partition.</p>"""
    column_name: "capo_glue.types.name_string.NameString"
    """<p>Name of the column.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteColumnStatisticsForPartitionRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    import capo_glue.types.value_string_list

    out["PartitionValues"] = capo_glue.types.value_string_list.serialize_aws_json_1_1(
        value["partition_values"]
    )
    out["ColumnName"] = value["column_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteColumnStatisticsForPartitionRequest:
    out: DeleteColumnStatisticsForPartitionRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForPartitionRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForPartitionRequest.table_name required"
        )
    if "PartitionValues" in data:
        import capo_glue.types.value_string_list

        out["partition_values"] = (
            capo_glue.types.value_string_list.deserialize_aws_json_1_1(
                data["PartitionValues"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForPartitionRequest.partition_values required"
        )
    if "ColumnName" in data:
        out["column_name"] = data["ColumnName"]
    else:
        raise DeserializationError(
            "DeleteColumnStatisticsForPartitionRequest.column_name required"
        )
    return out
