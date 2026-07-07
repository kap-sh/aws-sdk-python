"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteCustomDomainAssociationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.custom_domain_name_string
    import aws_sdk_redshift.types.string


class DeleteCustomDomainAssociationMessage(TypedDict, closed=True):
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The identifier of the cluster to delete a custom domain association for.</p>"""
    custom_domain_name: NotRequired[
        "aws_sdk_redshift.types.custom_domain_name_string.CustomDomainNameString"
    ]
    """<p>The custom domain name for the custom domain association.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCustomDomainAssociationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))
    if "custom_domain_name" in value:
        pairs.append((f"{prefix}.CustomDomainName", str(value["custom_domain_name"])))


def deserialize_query(el: Element) -> DeleteCustomDomainAssociationMessage:
    out: DeleteCustomDomainAssociationMessage = {}  # type: ignore[typeddict-item]
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    return out
