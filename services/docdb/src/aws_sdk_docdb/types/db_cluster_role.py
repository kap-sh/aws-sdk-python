"""Generated from Smithy shape ``com.amazonaws.docdb#DBClusterRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.string


class DBClusterRole(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAMrole that is associated with the DB cluster.</p>"""
    status: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>Describes the state of association between the IAMrole and the cluster. The <code>Status</code> property returns one of the following values:</p> <ul> <li> <p> <code>ACTIVE</code> - The IAMrole ARN is associated with the cluster and can be used to access other Amazon Web Services services on your behalf.</p> </li> <li> <p> <code>PENDING</code> - The IAMrole ARN is being associated with the cluster.</p> </li> <li> <p> <code>INVALID</code> - The IAMrole ARN is associated with the cluster, but the cluster cannot assume the IAMrole to access other Amazon Web Services services on your behalf.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


def deserialize_query(el: Element) -> DBClusterRole:
    out: DBClusterRole = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
