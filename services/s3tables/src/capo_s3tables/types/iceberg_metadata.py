"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.iceberg_partition_spec
    import capo_s3tables.types.iceberg_schema
    import capo_s3tables.types.iceberg_schema_v2
    import capo_s3tables.types.iceberg_sort_order
    import capo_s3tables.types.table_properties


class IcebergMetadata(TypedDict, closed=True):
    schema: NotRequired["capo_s3tables.types.iceberg_schema.IcebergSchema"]
    """<p>The schema for an Iceberg table. Use this property to define table schemas with primitive types only. For schemas that include nested or complex types such as <code>struct</code>, <code>list</code>, or <code>map</code>, use <code>schemaV2</code> instead.</p>"""
    schema_v2: NotRequired["capo_s3tables.types.iceberg_schema_v2.IcebergSchemaV2"]
    """<p>The schema for an Iceberg table using the V2 format. Use this property to define table schemas that include nested or complex data types such as <code>struct</code>, <code>list</code>, or <code>map</code>, in addition to primitive types. For schemas with only primitive types, you can use either <code>schema</code> or <code>schemaV2</code>.</p>"""
    partition_spec: NotRequired[
        "capo_s3tables.types.iceberg_partition_spec.IcebergPartitionSpec"
    ]
    """<p>The partition specification for the Iceberg table. Partitioning organizes data into separate files based on the values of one or more fields, which can improve query performance by reducing the amount of data scanned. Each partition field applies a transform (such as identity, year, month, or bucket) to a single field.</p>"""
    write_order: NotRequired["capo_s3tables.types.iceberg_sort_order.IcebergSortOrder"]
    """<p>The sort order for the Iceberg table. Sort order defines how data is sorted within data files, which can improve query performance by enabling more efficient data skipping and filtering.</p>"""
    properties: NotRequired["capo_s3tables.types.table_properties.TableProperties"]
    """<p>A map of custom configuration properties for the Iceberg table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IcebergMetadata) -> dict:
    out: dict = {}
    if "schema" in value:
        import capo_s3tables.types.iceberg_schema

        out["schema"] = capo_s3tables.types.iceberg_schema.serialize_json(
            value["schema"]
        )
    if "schema_v2" in value:
        import capo_s3tables.types.iceberg_schema_v2

        out["schemaV2"] = capo_s3tables.types.iceberg_schema_v2.serialize_json(
            value["schema_v2"]
        )
    if "partition_spec" in value:
        import capo_s3tables.types.iceberg_partition_spec

        out["partitionSpec"] = (
            capo_s3tables.types.iceberg_partition_spec.serialize_json(
                value["partition_spec"]
            )
        )
    if "write_order" in value:
        import capo_s3tables.types.iceberg_sort_order

        out["writeOrder"] = capo_s3tables.types.iceberg_sort_order.serialize_json(
            value["write_order"]
        )
    if "properties" in value:
        import capo_s3tables.types.table_properties

        out["properties"] = capo_s3tables.types.table_properties.serialize_json(
            value["properties"]
        )
    return out


def deserialize_json(data: dict) -> IcebergMetadata:
    out: IcebergMetadata = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        import capo_s3tables.types.iceberg_schema

        out["schema"] = capo_s3tables.types.iceberg_schema.deserialize_json(
            data["schema"]
        )
    if "schemaV2" in data:
        import capo_s3tables.types.iceberg_schema_v2

        out["schema_v2"] = capo_s3tables.types.iceberg_schema_v2.deserialize_json(
            data["schemaV2"]
        )
    if "partitionSpec" in data:
        import capo_s3tables.types.iceberg_partition_spec

        out["partition_spec"] = (
            capo_s3tables.types.iceberg_partition_spec.deserialize_json(
                data["partitionSpec"]
            )
        )
    if "writeOrder" in data:
        import capo_s3tables.types.iceberg_sort_order

        out["write_order"] = capo_s3tables.types.iceberg_sort_order.deserialize_json(
            data["writeOrder"]
        )
    if "properties" in data:
        import capo_s3tables.types.table_properties

        out["properties"] = capo_s3tables.types.table_properties.deserialize_json(
            data["properties"]
        )
    return out
