"""Generated from Smithy shape ``com.amazonaws.elasticache#GlobalReplicationGroupInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class GlobalReplicationGroupInfo(TypedDict):
    global_replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Global datastore</p>"""
    global_replication_group_member_role: NotRequired[
        "aws_sdk_elasticache.types.string.String"
    ]
    """<p>The role of the replication group in a Global datastore. Can be primary or secondary.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GlobalReplicationGroupInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "global_replication_group_id" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupId",
                str(value["global_replication_group_id"]),
            )
        )
    if "global_replication_group_member_role" in value:
        pairs.append(
            (
                f"{prefix}.GlobalReplicationGroupMemberRole",
                str(value["global_replication_group_member_role"]),
            )
        )


def deserialize_query(el: Element) -> GlobalReplicationGroupInfo:
    out: GlobalReplicationGroupInfo = {}  # type: ignore[typeddict-item]
    child_global_replication_group_id = el.find("GlobalReplicationGroupId")
    if child_global_replication_group_id is not None:
        out["global_replication_group_id"] = str(
            child_global_replication_group_id.text or ""
        )
    child_global_replication_group_member_role = el.find(
        "GlobalReplicationGroupMemberRole"
    )
    if child_global_replication_group_member_role is not None:
        out["global_replication_group_member_role"] = str(
            child_global_replication_group_member_role.text or ""
        )
    return out
