"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateRelationalDatabaseSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name
    import aws_sdk_lightsail.types.tag_list


class CreateRelationalDatabaseSnapshotRequest(TypedDict, closed=True):
    relational_database_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the database on which to base your new snapshot.</p>"""
    relational_database_snapshot_name: (
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    )
    """<p>The name for your new database snapshot.</p> <p>Constraints:</p> <ul> <li> <p>Must contain from 2 to 255 alphanumeric characters, or hyphens.</p> </li> <li> <p>The first and last character must be a letter or number.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRelationalDatabaseSnapshotRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseName"] = value["relational_database_name"]
    out["relationalDatabaseSnapshotName"] = value["relational_database_snapshot_name"]
    if "tags" in value:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRelationalDatabaseSnapshotRequest:
    out: CreateRelationalDatabaseSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseName" in data:
        out["relational_database_name"] = data["relationalDatabaseName"]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseSnapshotRequest.relational_database_name required"
        )
    if "relationalDatabaseSnapshotName" in data:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    else:
        raise DeserializationError(
            "CreateRelationalDatabaseSnapshotRequest.relational_database_snapshot_name required"
        )
    if "tags" in data:
        import aws_sdk_lightsail.types.tag_list

        out["tags"] = aws_sdk_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
