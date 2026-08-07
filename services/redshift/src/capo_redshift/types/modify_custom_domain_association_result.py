"""Generated from Smithy shape ``com.amazonaws.redshift#ModifyCustomDomainAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.custom_domain_certificate_arn_string
    import capo_redshift.types.custom_domain_name_string
    import capo_redshift.types.string


class ModifyCustomDomainAssociationResult(TypedDict, closed=True):
    custom_domain_name: NotRequired[
        "capo_redshift.types.custom_domain_name_string.CustomDomainNameString"
    ]
    """<p>The custom domain name associated with the result for the changed custom domain association.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "capo_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The certificate Amazon Resource Name (ARN) associated with the result for the changed custom domain association.</p>"""
    cluster_identifier: NotRequired["capo_redshift.types.string.String"]
    """<p>The identifier of the cluster associated with the result for the changed custom domain association.</p>"""
    custom_domain_cert_expiry_time: NotRequired["capo_redshift.types.string.String"]
    """<p>The certificate expiration time associated with the result for the changed custom domain association.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCustomDomainAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "custom_domain_name" in value:
        pairs.append(
            (f"{key_prefix}CustomDomainName", str(value["custom_domain_name"]))
        )
    if "custom_domain_certificate_arn" in value:
        pairs.append(
            (
                f"{key_prefix}CustomDomainCertificateArn",
                str(value["custom_domain_certificate_arn"]),
            )
        )
    if "cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}ClusterIdentifier", str(value["cluster_identifier"]))
        )
    if "custom_domain_cert_expiry_time" in value:
        pairs.append(
            (
                f"{key_prefix}CustomDomainCertExpiryTime",
                str(value["custom_domain_cert_expiry_time"]),
            )
        )


def deserialize_query(el: Element) -> ModifyCustomDomainAssociationResult:
    out: ModifyCustomDomainAssociationResult = {}  # type: ignore[typeddict-item]
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    child_custom_domain_certificate_arn = el.find("CustomDomainCertificateArn")
    if child_custom_domain_certificate_arn is not None:
        out["custom_domain_certificate_arn"] = str(
            child_custom_domain_certificate_arn.text or ""
        )
    child_cluster_identifier = el.find("ClusterIdentifier")
    if child_cluster_identifier is not None:
        out["cluster_identifier"] = str(child_cluster_identifier.text or "")
    child_custom_domain_cert_expiry_time = el.find("CustomDomainCertExpiryTime")
    if child_custom_domain_cert_expiry_time is not None:
        out["custom_domain_cert_expiry_time"] = str(
            child_custom_domain_cert_expiry_time.text or ""
        )
    return out
