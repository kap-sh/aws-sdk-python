"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#Database``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.date
    import aws_sdk_timestream_write.types.long
    import aws_sdk_timestream_write.types.resource_name
    import aws_sdk_timestream_write.types.string
    import aws_sdk_timestream_write.types.string_value2048


class Database(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_timestream_write.types.string.String"]
    """<p>The Amazon Resource Name that uniquely identifies this database.</p>"""
    database_name: NotRequired[
        "aws_sdk_timestream_write.types.resource_name.ResourceName"
    ]
    """<p>The name of the Timestream database.</p>"""
    table_count: "aws_sdk_timestream_write.types.long.Long"
    """<p>The total number of tables found within a Timestream database. </p>"""
    kms_key_id: NotRequired[
        "aws_sdk_timestream_write.types.string_value2048.StringValue2048"
    ]
    """<p>The identifier of the KMS key used to encrypt the data stored in the database.</p>"""
    creation_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p>The time when the database was created, calculated from the Unix epoch time.</p>"""
    last_updated_time: NotRequired["aws_sdk_timestream_write.types.date.Date"]
    """<p> The last time that this database was updated. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Database) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    out["TableCount"] = value.get("table_count", 0)
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "creation_time" in value:
        import aws_sdk_timestream_write.types.date

        out["CreationTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["creation_time"]
            )
        )
    if "last_updated_time" in value:
        import aws_sdk_timestream_write.types.date

        out["LastUpdatedTime"] = (
            aws_sdk_timestream_write.types.date.serialize_aws_json_1_0(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Database:
    out: Database = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    if "TableCount" in data:
        out["table_count"] = data["TableCount"]
    else:
        out["table_count"] = 0
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "CreationTime" in data:
        import aws_sdk_timestream_write.types.date

        out["creation_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["CreationTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_timestream_write.types.date

        out["last_updated_time"] = (
            aws_sdk_timestream_write.types.date.deserialize_aws_json_1_0(
                data["LastUpdatedTime"]
            )
        )
    return out
