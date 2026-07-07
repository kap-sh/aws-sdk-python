"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteRelationalDatabaseSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DeleteRelationalDatabaseSnapshotRequest(TypedDict, closed=True):
    relational_database_snapshot_name: (
        "aws_sdk_lightsail.types.resource_name.ResourceName"
    )
    """<p>The name of the database snapshot that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRelationalDatabaseSnapshotRequest) -> dict:
    out: dict = {}
    out["relationalDatabaseSnapshotName"] = value["relational_database_snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRelationalDatabaseSnapshotRequest:
    out: DeleteRelationalDatabaseSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseSnapshotName" in data:
        out["relational_database_snapshot_name"] = data[
            "relationalDatabaseSnapshotName"
        ]
    else:
        raise DeserializationError(
            "DeleteRelationalDatabaseSnapshotRequest.relational_database_snapshot_name required"
        )
    return out
