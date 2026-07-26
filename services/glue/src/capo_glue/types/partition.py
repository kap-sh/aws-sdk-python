"""Generated from Smithy shape ``com.amazonaws.glue#Partition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.parameters_map
    import capo_glue.types.storage_descriptor
    import capo_glue.types.timestamp
    import capo_glue.types.value_string_list


class Partition(TypedDict, closed=True):
    values: NotRequired["capo_glue.types.value_string_list.ValueStringList"]
    """<p>The values of the partition.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the catalog database in which to create the partition.</p>"""
    table_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the database table in which to create the partition.</p>"""
    creation_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time at which the partition was created.</p>"""
    last_access_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The last time at which the partition was accessed.</p>"""
    storage_descriptor: NotRequired[
        "capo_glue.types.storage_descriptor.StorageDescriptor"
    ]
    """<p>Provides information about the physical location where the partition is stored.</p>"""
    parameters: NotRequired["capo_glue.types.parameters_map.ParametersMap"]
    """<p>These key-value pairs define partition parameters.</p>"""
    last_analyzed_time: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The last time at which column statistics were computed for this partition.</p>"""
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which the partition resides.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Partition) -> dict:
    out: dict = {}
    if "values" in value:
        import capo_glue.types.value_string_list

        out["Values"] = capo_glue.types.value_string_list.serialize_aws_json_1_1(
            value["values"]
        )
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "creation_time" in value:
        import capo_glue.types.timestamp

        out["CreationTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_access_time" in value:
        import capo_glue.types.timestamp

        out["LastAccessTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_access_time"]
        )
    if "storage_descriptor" in value:
        import capo_glue.types.storage_descriptor

        out["StorageDescriptor"] = (
            capo_glue.types.storage_descriptor.serialize_aws_json_1_1(
                value["storage_descriptor"]
            )
        )
    if "parameters" in value:
        import capo_glue.types.parameters_map

        out["Parameters"] = capo_glue.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    if "last_analyzed_time" in value:
        import capo_glue.types.timestamp

        out["LastAnalyzedTime"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_analyzed_time"]
        )
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Partition:
    out: Partition = {}  # type: ignore[typeddict-item]
    if "Values" in data:
        import capo_glue.types.value_string_list

        out["values"] = capo_glue.types.value_string_list.deserialize_aws_json_1_1(
            data["Values"]
        )
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "CreationTime" in data:
        import capo_glue.types.timestamp

        out["creation_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastAccessTime" in data:
        import capo_glue.types.timestamp

        out["last_access_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastAccessTime"]
        )
    if "StorageDescriptor" in data:
        import capo_glue.types.storage_descriptor

        out["storage_descriptor"] = (
            capo_glue.types.storage_descriptor.deserialize_aws_json_1_1(
                data["StorageDescriptor"]
            )
        )
    if "Parameters" in data:
        import capo_glue.types.parameters_map

        out["parameters"] = capo_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    if "LastAnalyzedTime" in data:
        import capo_glue.types.timestamp

        out["last_analyzed_time"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastAnalyzedTime"]
        )
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    return out
