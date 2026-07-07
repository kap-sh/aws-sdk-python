"""Generated from Smithy shape ``com.amazonaws.keyspaces#SchemaDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_keyspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_keyspaces.types.clustering_key_list
    import aws_sdk_keyspaces.types.column_definition_list
    import aws_sdk_keyspaces.types.partition_key_list
    import aws_sdk_keyspaces.types.static_column_list


class SchemaDefinition(TypedDict, closed=True):
    all_columns: "aws_sdk_keyspaces.types.column_definition_list.ColumnDefinitionList"
    """<p>The regular columns of the table.</p>"""
    partition_keys: "aws_sdk_keyspaces.types.partition_key_list.PartitionKeyList"
    """<p>The columns that are part of the partition key of the table .</p>"""
    clustering_keys: NotRequired[
        "aws_sdk_keyspaces.types.clustering_key_list.ClusteringKeyList"
    ]
    """<p>The columns that are part of the clustering key of the table.</p>"""
    static_columns: NotRequired[
        "aws_sdk_keyspaces.types.static_column_list.StaticColumnList"
    ]
    """<p>The columns that have been defined as <code>STATIC</code>. Static columns store values that are shared by all rows in the same partition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SchemaDefinition) -> dict:
    out: dict = {}
    import aws_sdk_keyspaces.types.column_definition_list

    out["allColumns"] = (
        aws_sdk_keyspaces.types.column_definition_list.serialize_aws_json_1_0(
            value["all_columns"]
        )
    )
    import aws_sdk_keyspaces.types.partition_key_list

    out["partitionKeys"] = (
        aws_sdk_keyspaces.types.partition_key_list.serialize_aws_json_1_0(
            value["partition_keys"]
        )
    )
    if "clustering_keys" in value:
        import aws_sdk_keyspaces.types.clustering_key_list

        out["clusteringKeys"] = (
            aws_sdk_keyspaces.types.clustering_key_list.serialize_aws_json_1_0(
                value["clustering_keys"]
            )
        )
    if "static_columns" in value:
        import aws_sdk_keyspaces.types.static_column_list

        out["staticColumns"] = (
            aws_sdk_keyspaces.types.static_column_list.serialize_aws_json_1_0(
                value["static_columns"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SchemaDefinition:
    out: SchemaDefinition = {}  # type: ignore[typeddict-item]
    if "allColumns" in data:
        import aws_sdk_keyspaces.types.column_definition_list

        out["all_columns"] = (
            aws_sdk_keyspaces.types.column_definition_list.deserialize_aws_json_1_0(
                data["allColumns"]
            )
        )
    else:
        raise DeserializationError("SchemaDefinition.all_columns required")
    if "partitionKeys" in data:
        import aws_sdk_keyspaces.types.partition_key_list

        out["partition_keys"] = (
            aws_sdk_keyspaces.types.partition_key_list.deserialize_aws_json_1_0(
                data["partitionKeys"]
            )
        )
    else:
        raise DeserializationError("SchemaDefinition.partition_keys required")
    if "clusteringKeys" in data:
        import aws_sdk_keyspaces.types.clustering_key_list

        out["clustering_keys"] = (
            aws_sdk_keyspaces.types.clustering_key_list.deserialize_aws_json_1_0(
                data["clusteringKeys"]
            )
        )
    if "staticColumns" in data:
        import aws_sdk_keyspaces.types.static_column_list

        out["static_columns"] = (
            aws_sdk_keyspaces.types.static_column_list.deserialize_aws_json_1_0(
                data["staticColumns"]
            )
        )
    return out
