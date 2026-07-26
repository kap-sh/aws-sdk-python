"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterIamRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.cluster_iam_role

ClusterIamRoleList: TypeAlias = list[
    "capo_redshift.types.cluster_iam_role.ClusterIamRole"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterIamRoleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_iam_role

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_iam_role.serialize_query(
            item, pairs, f"{prefix}.ClusterIamRole.{n}"
        )


def deserialize_query(el: Element) -> ClusterIamRoleList:
    import capo_redshift.types.cluster_iam_role

    out: ClusterIamRoleList = []
    for child in el.findall("ClusterIamRole"):
        out.append(capo_redshift.types.cluster_iam_role.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ClusterIamRoleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.cluster_iam_role

    for n, item in enumerate(value, 1):
        capo_redshift.types.cluster_iam_role.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ClusterIamRoleList:
    import capo_redshift.types.cluster_iam_role

    out: ClusterIamRoleList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.cluster_iam_role.deserialize_query(child))
    return out
