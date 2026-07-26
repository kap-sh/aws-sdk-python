"""Generated from Smithy shape ``com.amazonaws.lightsail#GetRelationalDatabaseSnapshotResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.relational_database_snapshot


class GetRelationalDatabaseSnapshotResult(TypedDict, closed=True):
    relational_database_snapshot: NotRequired[
        "capo_lightsail.types.relational_database_snapshot.RelationalDatabaseSnapshot"
    ]
    """<p>An object describing the specified database snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRelationalDatabaseSnapshotResult) -> dict:
    out: dict = {}
    if "relational_database_snapshot" in value:
        import capo_lightsail.types.relational_database_snapshot

        out["relationalDatabaseSnapshot"] = (
            capo_lightsail.types.relational_database_snapshot.serialize_aws_json_1_1(
                value["relational_database_snapshot"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRelationalDatabaseSnapshotResult:
    out: GetRelationalDatabaseSnapshotResult = {}  # type: ignore[typeddict-item]
    if "relationalDatabaseSnapshot" in data:
        import capo_lightsail.types.relational_database_snapshot

        out["relational_database_snapshot"] = (
            capo_lightsail.types.relational_database_snapshot.deserialize_aws_json_1_1(
                data["relationalDatabaseSnapshot"]
            )
        )
    return out
