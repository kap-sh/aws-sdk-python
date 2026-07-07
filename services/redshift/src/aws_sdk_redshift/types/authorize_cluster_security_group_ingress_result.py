"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeClusterSecurityGroupIngressResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_security_group


class AuthorizeClusterSecurityGroupIngressResult(TypedDict, closed=True):
    cluster_security_group: NotRequired[
        "aws_sdk_redshift.types.cluster_security_group.ClusterSecurityGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeClusterSecurityGroupIngressResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_security_group" in value:
        import aws_sdk_redshift.types.cluster_security_group

        aws_sdk_redshift.types.cluster_security_group.serialize_query(
            value["cluster_security_group"], pairs, f"{prefix}.ClusterSecurityGroup"
        )


def deserialize_query(el: Element) -> AuthorizeClusterSecurityGroupIngressResult:
    out: AuthorizeClusterSecurityGroupIngressResult = {}  # type: ignore[typeddict-item]
    child_cluster_security_group = el.find("ClusterSecurityGroup")
    if child_cluster_security_group is not None:
        import aws_sdk_redshift.types.cluster_security_group

        out["cluster_security_group"] = (
            aws_sdk_redshift.types.cluster_security_group.deserialize_query(
                child_cluster_security_group
            )
        )
    return out
