"""Generated from Smithy shape ``com.amazonaws.redshift#AuthorizeEndpointAccessMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string
    import capo_redshift.types.vpc_identifier_list


class AuthorizeEndpointAccessMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The cluster identifier of the cluster to grant access to.</p>"""
    account: NotRequired["capo_redshift.types.string.String"]
    """<p>The Amazon Web Services account ID to grant access to.</p>"""
    vpc_ids: NotRequired["capo_redshift.types.vpc_identifier_list.VpcIdentifierList"]
    """<p>The virtual private cloud (VPC) identifiers to grant access to.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AuthorizeEndpointAccessMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "account" in value:
        pairs.append((f"{key_prefix}Account", str(value["account"])))
    if "vpc_ids" in value:
        import capo_redshift.types.vpc_identifier_list

        capo_redshift.types.vpc_identifier_list.serialize_query(
            value["vpc_ids"], pairs, f"{key_prefix}VpcIds"
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
        import capo_redshift.types.vpc_identifier_list

        out["vpc_ids"] = capo_redshift.types.vpc_identifier_list.deserialize_query(
            child_vpc_ids
        )
    return out
