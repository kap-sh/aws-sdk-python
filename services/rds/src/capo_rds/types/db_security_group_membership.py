"""Generated from Smithy shape ``com.amazonaws.rds#DBSecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DBSecurityGroupMembership(TypedDict, closed=True):
    db_security_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the DB security group.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the DB security group.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroupMembership, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_security_group_name" in value:
        pairs.append(
            (f"{key_prefix}DBSecurityGroupName", str(value["db_security_group_name"]))
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> DBSecurityGroupMembership:
    out: DBSecurityGroupMembership = {}  # type: ignore[typeddict-item]
    child_db_security_group_name = el.find("DBSecurityGroupName")
    if child_db_security_group_name is not None:
        out["db_security_group_name"] = str(child_db_security_group_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
