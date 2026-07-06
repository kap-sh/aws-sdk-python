"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#CreateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.magnetic_store_write_properties
    import aws_sdk_timestream_write.types.resource_create_api_name
    import aws_sdk_timestream_write.types.retention_properties
    import aws_sdk_timestream_write.types.schema
    import aws_sdk_timestream_write.types.tag_list


class CreateTableRequest(TypedDict, closed=True):
    database_name: (
        "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>The name of the Timestream database.</p>"""
    table_name: (
        "aws_sdk_timestream_write.types.resource_create_api_name.ResourceCreateAPIName"
    )
    """<p>The name of the Timestream table.</p>"""
    retention_properties: NotRequired[
        "aws_sdk_timestream_write.types.retention_properties.RetentionProperties"
    ]
    """<p>The duration for which your time-series data must be stored in the memory store and the magnetic store.</p>"""
    tags: NotRequired["aws_sdk_timestream_write.types.tag_list.TagList"]
    """<p> A list of key-value pairs to label the table. </p>"""
    magnetic_store_write_properties: NotRequired[
        "aws_sdk_timestream_write.types.magnetic_store_write_properties.MagneticStoreWriteProperties"
    ]
    """<p>Contains properties to set on the table when enabling magnetic store writes.</p>"""
    schema: NotRequired["aws_sdk_timestream_write.types.schema.Schema"]
    """<p> The schema of the table. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateTableRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "retention_properties" in value:
        import aws_sdk_timestream_write.types.retention_properties

        out["RetentionProperties"] = (
            aws_sdk_timestream_write.types.retention_properties.serialize_aws_json_1_0(
                value["retention_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_timestream_write.types.tag_list

        out["Tags"] = aws_sdk_timestream_write.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "magnetic_store_write_properties" in value:
        import aws_sdk_timestream_write.types.magnetic_store_write_properties

        out["MagneticStoreWriteProperties"] = (
            aws_sdk_timestream_write.types.magnetic_store_write_properties.serialize_aws_json_1_0(
                value["magnetic_store_write_properties"]
            )
        )
    if "schema" in value:
        import aws_sdk_timestream_write.types.schema

        out["Schema"] = aws_sdk_timestream_write.types.schema.serialize_aws_json_1_0(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateTableRequest:
    out: CreateTableRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("CreateTableRequest.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("CreateTableRequest.table_name required")
    if "RetentionProperties" in data:
        import aws_sdk_timestream_write.types.retention_properties

        out["retention_properties"] = (
            aws_sdk_timestream_write.types.retention_properties.deserialize_aws_json_1_0(
                data["RetentionProperties"]
            )
        )
    if "Tags" in data:
        import aws_sdk_timestream_write.types.tag_list

        out["tags"] = aws_sdk_timestream_write.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "MagneticStoreWriteProperties" in data:
        import aws_sdk_timestream_write.types.magnetic_store_write_properties

        out["magnetic_store_write_properties"] = (
            aws_sdk_timestream_write.types.magnetic_store_write_properties.deserialize_aws_json_1_0(
                data["MagneticStoreWriteProperties"]
            )
        )
    if "Schema" in data:
        import aws_sdk_timestream_write.types.schema

        out["schema"] = aws_sdk_timestream_write.types.schema.deserialize_aws_json_1_0(
            data["Schema"]
        )
    return out
