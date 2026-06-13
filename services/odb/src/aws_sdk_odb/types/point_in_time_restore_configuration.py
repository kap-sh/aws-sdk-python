"""Generated from Smithy shape ``com.amazonaws.odb#PointInTimeRestoreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.clone_type
    import aws_sdk_odb.types.integer_list
    import aws_sdk_odb.types.resource_id_or_arn


class PointInTimeRestoreConfiguration(TypedDict):
    source_autonomous_database_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the source Autonomous Database to restore from.</p>"""
    clone_type: "aws_sdk_odb.types.clone_type.CloneType"
    """<p>The type of clone to create from the point-in-time restore.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The date and time to which to restore the Autonomous Database.</p>"""
    use_latest_available_backup_timestamp: NotRequired["bool"]
    """<p>Indicates whether to use the latest available backup timestamp for the restore.</p>"""
    clone_table_space_list: NotRequired["aws_sdk_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone from the point-in-time restore.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRestoreConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    import aws_sdk_odb.types.clone_type

    out["cloneType"] = aws_sdk_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    if "timestamp" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timestamp"] = aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "use_latest_available_backup_timestamp" in value:
        out["useLatestAvailableBackupTimestamp"] = value[
            "use_latest_available_backup_timestamp"
        ]
    if "clone_table_space_list" in value:
        import aws_sdk_odb.types.integer_list

        out["cloneTableSpaceList"] = (
            aws_sdk_odb.types.integer_list.serialize_aws_json_1_0(
                value["clone_table_space_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRestoreConfiguration:
    out: PointInTimeRestoreConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceAutonomousDatabaseId" in data:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        raise DeserializationError(
            "PointInTimeRestoreConfiguration.source_autonomous_database_id required"
        )
    if "cloneType" in data:
        import aws_sdk_odb.types.clone_type

        out["clone_type"] = aws_sdk_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        raise DeserializationError(
            "PointInTimeRestoreConfiguration.clone_type required"
        )
    if "timestamp" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timestamp"]
            )
        )
    if "useLatestAvailableBackupTimestamp" in data:
        out["use_latest_available_backup_timestamp"] = data[
            "useLatestAvailableBackupTimestamp"
        ]
    if "cloneTableSpaceList" in data:
        import aws_sdk_odb.types.integer_list

        out["clone_table_space_list"] = (
            aws_sdk_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    return out
