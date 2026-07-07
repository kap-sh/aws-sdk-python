"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.vpc_identifier_list


class AuthorizeEndpointAccessMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster identifier of the cluster to grant access to.</p>"""
    account: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID to grant access to.</p>"""
    vpc_ids: NotRequired["aws_sdk_redshift.types.vpc_identifier_list.VpcIdentifierList"]
    """<p>The virtual private cloud (VPC) identifiers to grant access to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
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


def deserialize_query(el: Element) -> AuthorizeEndpointAccessMessage:
    out: AuthorizeEndpointAccessMessage = {}  # type: ignore[typeddict-item]
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
    return out
