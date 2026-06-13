"""Generated from Smithy shape ``com.amazonaws.odb#RestoreFromBackupConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.clone_type
    import aws_sdk_odb.types.integer_list
    import aws_sdk_odb.types.resource_id_or_arn


class RestoreFromBackupConfiguration(TypedDict):
    autonomous_database_backup_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the Autonomous Database backup to restore from.</p>"""
    clone_type: "aws_sdk_odb.types.clone_type.CloneType"
    """<p>The type of clone to create from the backup.</p>"""
    clone_table_space_list: NotRequired["aws_sdk_odb.types.integer_list.IntegerList"]
    """<p>The list of tablespace identifiers to clone from the backup.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFromBackupConfiguration) -> dict:
    out: dict = {}
    out["autonomousDatabaseBackupId"] = value["autonomous_database_backup_id"]
    import aws_sdk_odb.types.clone_type

    out["cloneType"] = aws_sdk_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    if "clone_table_space_list" in value:
        import aws_sdk_odb.types.integer_list

        out["cloneTableSpaceList"] = (
            aws_sdk_odb.types.integer_list.serialize_aws_json_1_0(
                value["clone_table_space_list"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFromBackupConfiguration:
    out: RestoreFromBackupConfiguration = {}  # type: ignore[typeddict-item]
    if "autonomousDatabaseBackupId" in data:
        out["autonomous_database_backup_id"] = data["autonomousDatabaseBackupId"]
    else:
        raise DeserializationError(
            "RestoreFromBackupConfiguration.autonomous_database_backup_id required"
        )
    if "cloneType" in data:
        import aws_sdk_odb.types.clone_type

        out["clone_type"] = aws_sdk_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        raise DeserializationError("RestoreFromBackupConfiguration.clone_type required")
    if "cloneTableSpaceList" in data:
        import aws_sdk_odb.types.integer_list

        out["clone_table_space_list"] = (
            aws_sdk_odb.types.integer_list.deserialize_aws_json_1_0(
                data["cloneTableSpaceList"]
            )
        )
    return out
