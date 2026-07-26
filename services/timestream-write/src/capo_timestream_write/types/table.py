"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Table``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_write.types.date
    import capo_timestream_write.types.magnetic_store_write_properties
    import capo_timestream_write.types.resource_name
    import capo_timestream_write.types.retention_properties
    import capo_timestream_write.types.schema
    import capo_timestream_write.types.string
    import capo_timestream_write.types.table_status


class Table(TypedDict, closed=True):
    arn: NotRequired["capo_timestream_write.types.string.String"]
    """<p>The Amazon Resource Name that uniquely identifies this table.</p>"""
    table_name: NotRequired["capo_timestream_write.types.resource_name.ResourceName"]
    """<p>The name of the Timestream table.</p>"""
    database_name: NotRequired["capo_timestream_write.types.resource_name.ResourceName"]
    """<p>The name of the Timestream database that contains this table.</p>"""
    table_status: NotRequired["capo_timestream_write.types.table_status.TableStatus"]
    """<p>The current state of the table:</p> <ul> <li> <p> <code>DELETING</code> - The table is being deleted.</p> </li> <li> <p> <code>ACTIVE</code> - The table is ready for use.</p> </li> </ul>"""
    retention_properties: NotRequired[
        "capo_timestream_write.types.retention_properties.RetentionProperties"
    ]
    """<p>The retention duration for the memory store and magnetic store.</p>"""
    creation_time: NotRequired["capo_timestream_write.types.date.Date"]
    """<p>The time when the Timestream table was created. </p>"""
    last_updated_time: NotRequired["capo_timestream_write.types.date.Date"]
    """<p>The time when the Timestream table was last updated.</p>"""
    magnetic_store_write_properties: NotRequired[
        "capo_timestream_write.types.magnetic_store_write_properties.MagneticStoreWriteProperties"
    ]
    """<p>Contains properties to set on the table when enabling magnetic store writes.</p>"""
    schema: NotRequired["capo_timestream_write.types.schema.Schema"]
    """<p> The schema of the table. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Table) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_status" in value:
        import capo_timestream_write.types.table_status

        out["TableStatus"] = (
            capo_timestream_write.types.table_status.serialize_aws_json_1_0(
                value["table_status"]
            )
        )
    if "retention_properties" in value:
        import capo_timestream_write.types.retention_properties

        out["RetentionProperties"] = (
            capo_timestream_write.types.retention_properties.serialize_aws_json_1_0(
                value["retention_properties"]
            )
        )
    if "creation_time" in value:
        import capo_timestream_write.types.date

        out["CreationTime"] = capo_timestream_write.types.date.serialize_aws_json_1_0(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_timestream_write.types.date

        out["LastUpdatedTime"] = (
            capo_timestream_write.types.date.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    if "magnetic_store_write_properties" in value:
        import capo_timestream_write.types.magnetic_store_write_properties

        out["MagneticStoreWriteProperties"] = (
            capo_timestream_write.types.magnetic_store_write_properties.serialize_aws_json_1_0(
                value["magnetic_store_write_properties"]
            )
        )
    if "schema" in value:
        import capo_timestream_write.types.schema

        out["Schema"] = capo_timestream_write.types.schema.serialize_aws_json_1_0(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Table:
    out: Table = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableStatus" in data:
        import capo_timestream_write.types.table_status

        out["table_status"] = (
            capo_timestream_write.types.table_status.deserialize_aws_json_1_0(
                data["TableStatus"]
            )
        )
    if "RetentionProperties" in data:
        import capo_timestream_write.types.retention_properties

        out["retention_properties"] = (
            capo_timestream_write.types.retention_properties.deserialize_aws_json_1_0(
                data["RetentionProperties"]
            )
        )
    if "CreationTime" in data:
        import capo_timestream_write.types.date

        out["creation_time"] = (
            capo_timestream_write.types.date.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import capo_timestream_write.types.date

        out["last_updated_time"] = (
            capo_timestream_write.types.date.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    if "MagneticStoreWriteProperties" in data:
        import capo_timestream_write.types.magnetic_store_write_properties

        out["magnetic_store_write_properties"] = (
            capo_timestream_write.types.magnetic_store_write_properties.deserialize_aws_json_1_0(
                data["MagneticStoreWriteProperties"]
            )
        )
    if "Schema" in data:
        import capo_timestream_write.types.schema

        out["schema"] = capo_timestream_write.types.schema.deserialize_aws_json_1_0(
            data["Schema"]
        )
    return out
