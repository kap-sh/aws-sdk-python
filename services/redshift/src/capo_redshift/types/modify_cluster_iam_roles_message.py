"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyClusterIamRolesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.iam_role_arn_list
    import capo_redshift.types.string


class ModifyClusterIamRolesMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The unique identifier of the cluster for which you want to associate or disassociate IAM roles.</p>"""
    add_iam_roles: NotRequired["capo_redshift.types.iam_role_arn_list.IamRoleArnList"]
    """<p>Zero or more IAM roles to associate with the cluster. The roles must be in their Amazon Resource Name (ARN) format. </p>"""
    remove_iam_roles: NotRequired[
        "capo_redshift.types.iam_role_arn_list.IamRoleArnList"
    ]
    """<p>Zero or more IAM roles in ARN format to disassociate from the cluster. </p>"""
    default_iam_role_arn: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the IAM role that was set as default for the cluster when the cluster was last modified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyClusterIamRolesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "add_iam_roles" in value:
        import capo_redshift.types.iam_role_arn_list

        capo_redshift.types.iam_role_arn_list.serialize_query(
            value["add_iam_roles"], pairs, f"{prefix}.AddIamRoles"
        )
    if "remove_iam_roles" in value:
        import capo_redshift.types.iam_role_arn_list

        capo_redshift.types.iam_role_arn_list.serialize_query(
            value["remove_iam_roles"], pairs, f"{prefix}.RemoveIamRoles"
        )
    if "default_iam_role_arn" in value:
        pairs.append(
            (f"{prefix}.DefaultIamRoleArn", str(value["default_iam_role_arn"]))
        )


def deserialize_query(el: Element) -> ModifyClusterIamRolesMessage:
    out: ModifyClusterIamRolesMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_add_iam_roles = el.find("AddIamRoles")
    if child_add_iam_roles is not None:
        import capo_redshift.types.iam_role_arn_list

        out["add_iam_roles"] = capo_redshift.types.iam_role_arn_list.deserialize_query(
            child_add_iam_roles
        )
    child_remove_iam_roles = el.find("RemoveIamRoles")
    if child_remove_iam_roles is not None:
        import capo_redshift.types.iam_role_arn_list

        out["remove_iam_roles"] = (
            capo_redshift.types.iam_role_arn_list.deserialize_query(
                child_remove_iam_roles
            )
        )
    child_default_iam_role_arn = el.find("DefaultIamRoleArn")
    if child_default_iam_role_arn is not None:
        out["default_iam_role_arn"] = str(child_default_iam_role_arn.text or "")
    return out
