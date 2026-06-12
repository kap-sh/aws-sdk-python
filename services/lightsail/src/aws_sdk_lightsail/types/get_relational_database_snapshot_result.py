"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseSnapshotResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.relational_database_snapshot


class GetRelationalDatabaseSnapshotResult(TypedDict):
    relational_database_snapshot: NotRequired[
        "aws_sdk_lightsail.types.relational_database_snapshot.RelationalDatabaseSnapshot"
    ]
    """<p>An object describing the specified database snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseSnapshotResult) -> dict:
    out: dict = {}
    if "relational_database_snapshot" in value:
        import aws_sdk_lightsail.types.relational_database_snapshot

        out["relationalDatabaseSnapshot"] = (
            aws_sdk_lightsail.types.relational_database_snapshot.serialize_aws_json_1_1(
                value["relational_database_snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseSnapshotResult:
    out: GetRelationalDatabaseSnapshotResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseSnapshot" in data:
        import aws_sdk_lightsail.types.relational_database_snapshot

        out["relational_database_snapshot"] = (
            aws_sdk_lightsail.types.relational_database_snapshot.deserialize_aws_json_1_1(
                data["relationalDatabaseSnapshot"]
            )
        )
    return out
