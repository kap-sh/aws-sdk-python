"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseCloneConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.clone_type
    import aws_sdk_odb.types.resource_id_or_arn


class DatabaseCloneConfiguration(TypedDict):
    source_autonomous_database_id: (
        "aws_sdk_odb.types.resource_id_or_arn.ResourceIdOrArn"
    )
    """<p>The unique identifier of the source Autonomous Database to clone.</p>"""
    clone_type: "aws_sdk_odb.types.clone_type.CloneType"
    """<p>The type of clone to create, either a full clone, a metadata clone, or a partial clone.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseCloneConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseId"] = value["source_autonomous_database_id"]
    import aws_sdk_odb.types.clone_type

    out["cloneType"] = aws_sdk_odb.types.clone_type.serialize_aws_json_1_0(
        value["clone_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatabaseCloneConfiguration:
    out: DatabaseCloneConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceAutonomousDatabaseId" in data:
        out["source_autonomous_database_id"] = data["sourceAutonomousDatabaseId"]
    else:
        raise DeserializationError(
            "DatabaseCloneConfiguration.source_autonomous_database_id required"
        )
    if "cloneType" in data:
        import aws_sdk_odb.types.clone_type

        out["clone_type"] = aws_sdk_odb.types.clone_type.deserialize_aws_json_1_0(
            data["cloneType"]
        )
    else:
        raise DeserializationError("DatabaseCloneConfiguration.clone_type required")
    return out
