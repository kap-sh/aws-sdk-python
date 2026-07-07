"""Generated from Smithy shape ``com.amazonaws.redshift#Association``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.certificate_association_list
    import aws_sdk_redshift.types.string
    import aws_sdk_redshift.types.t_stamp


class Association(TypedDict, closed=True):
    custom_domain_certificate_arn: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The Amazon Resource Name (ARN) for the certificate associated with the custom domain.</p>"""
    custom_domain_certificate_expiry_date: NotRequired[
        "aws_sdk_redshift.types.t_stamp.TStamp"
    ]
    """<p>The expiration date for the certificate.</p>"""
    certificate_associations: NotRequired[
        "aws_sdk_redshift.types.certificate_association_list.CertificateAssociationList"
    ]
    """<p>A list of all associated clusters and domain names tied to a specific certificate.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: Association, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "custom_domain_certificate_arn" in value:
        pairs.append(
            (
                f"{prefix}.CustomDomainCertificateArn",
                str(value["custom_domain_certificate_arn"]),
            )
        )
    if "custom_domain_certificate_expiry_date" in value:
        import aws_sdk_redshift.types.t_stamp

        aws_sdk_redshift.types.t_stamp.serialize_query(
            value["custom_domain_certificate_expiry_date"],
            pairs,
            f"{prefix}.CustomDomainCertificateExpiryDate",
        )
    if "certificate_associations" in value:
        import aws_sdk_redshift.types.certificate_association_list

        aws_sdk_redshift.types.certificate_association_list.serialize_query(
            value["certificate_associations"],
            pairs,
            f"{prefix}.CertificateAssociations",
        )


def deserialize_query(el: Element) -> Association:
    out: Association = {}  # type: ignore[typeddict-item]
    child_custom_domain_certificate_arn = el.find("CustomDomainCertificateArn")
    if child_custom_domain_certificate_arn is not None:
        out["custom_domain_certificate_arn"] = str(
            child_custom_domain_certificate_arn.text or ""
        )
    child_custom_domain_certificate_expiry_date = el.find(
        "CustomDomainCertificateExpiryDate"
    )
    if child_custom_domain_certificate_expiry_date is not None:
        import aws_sdk_redshift.types.t_stamp

        out["custom_domain_certificate_expiry_date"] = (
            aws_sdk_redshift.types.t_stamp.deserialize_query(
                child_custom_domain_certificate_expiry_date
            )
        )
    child_certificate_associations = el.find("CertificateAssociations")
    if child_certificate_associations is not None:
        import aws_sdk_redshift.types.certificate_association_list

        out["certificate_associations"] = (
            aws_sdk_redshift.types.certificate_association_list.deserialize_query(
                child_certificate_associations
            )
        )
    return out
