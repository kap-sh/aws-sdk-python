"""Generated from Smithy shape ``com.amazonaws.rds#RebootDBShardGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.db_shard_group_identifier


class RebootDBShardGroupMessage(TypedDict):
    db_shard_group_identifier: NotRequired[
        "aws_sdk_rds.types.db_shard_group_identifier.DBShardGroupIdentifier"
    ]
    """<p>The name of the DB shard group to reboot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RebootDBShardGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_shard_group_identifier" in value:
        pairs.append(
            (
                f"{prefix}.DBShardGroupIdentifier",
                str(value["db_shard_group_identifier"]),
            )
        )


def deserialize_query(el: Element) -> RebootDBShardGroupMessage:
    out: RebootDBShardGroupMessage = {}  # type: ignore[typeddict-item]
    child_db_shard_group_identifier = el.find("DBShardGroupIdentifier")
    if child_db_shard_group_identifier is not None:
        out["db_shard_group_identifier"] = str(
            child_db_shard_group_identifier.text or ""
        )
    return out
