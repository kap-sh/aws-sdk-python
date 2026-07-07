"""Generated from Smithy shape ``com.amazonaws.elasticache#StartMigrationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.replication_group


class StartMigrationResponse(TypedDict, closed=True):
    replication_group: NotRequired[
        "aws_sdk_elasticache.types.replication_group.ReplicationGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: StartMigrationResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group" in value:
        import aws_sdk_elasticache.types.replication_group

        aws_sdk_elasticache.types.replication_group.serialize_query(
            value["replication_group"], pairs, f"{prefix}.ReplicationGroup"
        )


def deserialize_query(el: Element) -> StartMigrationResponse:
    out: StartMigrationResponse = {}  # type: ignore[typeddict-item]
    child_replication_group = el.find("ReplicationGroup")
    if child_replication_group is not None:
        import aws_sdk_elasticache.types.replication_group

        out["replication_group"] = (
            aws_sdk_elasticache.types.replication_group.deserialize_query(
                child_replication_group
            )
        )
    return out
