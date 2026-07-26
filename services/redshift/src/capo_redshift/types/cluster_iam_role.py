"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterIamRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class ClusterIamRole(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the IAM role, for example, <code>arn:aws:iam::123456789012:role/RedshiftCopyUnload</code>. </p>"""
    apply_status: NotRequired["capo_redshift.types.string.String"]
    """<p>A value that describes the status of the IAM role's association with an Amazon Redshift cluster.</p> <p>The following are possible statuses and descriptions.</p> <ul> <li> <p> <code>in-sync</code>: The role is available for use by the cluster.</p> </li> <li> <p> <code>adding</code>: The role is in the process of being associated with the cluster.</p> </li> <li> <p> <code>removing</code>: The role is in the process of being disassociated with the cluster.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterIamRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "iam_role_arn" in value:
        pairs.append((f"{prefix}.IamRoleArn", str(value["iam_role_arn"])))
    if "apply_status" in value:
        pairs.append((f"{prefix}.ApplyStatus", str(value["apply_status"])))


def deserialize_query(el: Element) -> ClusterIamRole:
    out: ClusterIamRole = {}  # type: ignore[typeddict-item]
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    child_apply_status = el.find("ApplyStatus")
    if child_apply_status is not None:
        out["apply_status"] = str(child_apply_status.text or "")
    return out
