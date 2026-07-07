"""Generated from Smithy shape ``com.amazonaws.redshift#CertificateAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.string


class CertificateAssociation(TypedDict, closed=True):
    custom_domain_name: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The custom domain name for the certificate association.</p>"""
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster identifier for the certificate association.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CertificateAssociation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "custom_domain_name" in value:
        pairs.append((f"{prefix}.CustomDomainName", str(value["custom_domain_name"])))
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))


def deserialize_query(el: Element) -> CertificateAssociation:
    out: CertificateAssociation = {}  # type: ignore[typeddict-item]
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    return out
