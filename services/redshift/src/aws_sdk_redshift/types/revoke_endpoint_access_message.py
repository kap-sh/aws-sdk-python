"""Generated from Smithy shape ``com.amazonaws.redshift#RevokeEndpointAccessMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.boolean
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.vpc_identifier_list


class RevokeEndpointAccessMessage(TypedDict):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster to revoke access from.</p>"""
    account: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID whose access is to be revoked.</p>"""
    vpc_ids: NotRequired["aws_sdk_redshift.types.vpc_identifier_list.VpcIdentifierList"]
    """<p>The virtual private cloud (VPC) identifiers for which access is to be revoked.</p>"""
    force: NotRequired["aws_sdk_redshift.types.boolean.Boolean"]
    """<p>Indicates whether to force the revoke action. If true, the Redshift-managed VPC endpoints associated with the endpoint authorization are also deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RevokeEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "account" in value:
        pairs.append((f"{prefix}.Account", str(value["account"])))
    if "vpc_ids" in value:
        import aws_sdk_redshift.types.vpc_identifier_list

        aws_sdk_redshift.types.vpc_identifier_list.serialize_query(
            value["vpc_ids"], pairs, f"{prefix}.VpcIds"
        )
    if "force" in value:
        pairs.append((f"{prefix}.Force", "true" if value["force"] else "false"))


def deserialize_query(el: Element) -> RevokeEndpointAccessMessage:
    out: RevokeEndpointAccessMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_account = el.find("Account")
    if child_account is not None:
        out["account"] = str(child_account.text or "")
    child_vpc_ids = el.find("VpcIds")
    if child_vpc_ids is not None:
        import aws_sdk_redshift.types.vpc_identifier_list

        out["vpc_ids"] = aws_sdk_redshift.types.vpc_identifier_list.deserialize_query(
            child_vpc_ids
        )
    child_force = el.find("Force")
    if child_force is not None:
        out["force"] = (child_force.text or "").lower() == "true"
    return out
