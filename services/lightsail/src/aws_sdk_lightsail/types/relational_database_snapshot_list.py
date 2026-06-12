"""Generated from Smithy shape ``com.amazonaws.lightsail#RelationalDatabaseSnapshotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_snapshot

RelationalDatabaseSnapshotList: TypeAlias = list[
    "aws_sdk_lightsail.types.relational_database_snapshot.RelationalDatabaseSnapshot"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RelationalDatabaseSnapshotList) -> list:
    import aws_sdk_lightsail.types.relational_database_snapshot

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.relational_database_snapshot.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RelationalDatabaseSnapshotList:
    import aws_sdk_lightsail.types.relational_database_snapshot

    out: RelationalDatabaseSnapshotList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.relational_database_snapshot.deserialize_aws_json_1_1(
                item
            )
        )
    return out
