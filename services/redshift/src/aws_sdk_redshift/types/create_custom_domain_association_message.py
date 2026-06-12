"""Generated from Smithy shape ``com.amazonaws.redshift#CreateCustomDomainAssociationMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.custom_domain_certificate_arn_string
    import aws_sdk_redshift.types.custom_domain_name_string
    import aws_sdk_redshift.types.string


class CreateCustomDomainAssociationMessage(TypedDict):
    custom_domain_name: NotRequired[
        "aws_sdk_redshift.types.custom_domain_name_string.CustomDomainNameString"
    ]
    """<p>The custom domain name for a custom domain association.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "aws_sdk_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The certificate Amazon Resource Name (ARN) for the custom domain name association.</p>"""
    cluster_identifier: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The cluster identifier that the custom domain is associated with.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCustomDomainAssociationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "custom_domain_name" in value:
        pairs.append((f"{prefix}.CustomDomainName", str(value["custom_domain_name"])))
    if "custom_domain_certificate_arn" in value:
        pairs.append(
            (
                f"{prefix}.CustomDomainCertificateArn",
                str(value["custom_domain_certificate_arn"]),
            )
        )
    if "cluster_identifier" in value:
        pairs.append((f"{prefix}.ClusterIdentifier", str(value["cluster_identifier"])))


def deserialize_query(el: Element) -> CreateCustomDomainAssociationMessage:
    out: CreateCustomDomainAssociationMessage = {}  # type: ignore[typeddict-item]
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
    return out
