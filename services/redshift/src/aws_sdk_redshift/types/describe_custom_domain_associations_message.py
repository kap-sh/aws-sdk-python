"""Generated from Smithy shape ``com.amazonaws.redshift#DescribeCustomDomainAssociationsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.custom_domain_certificate_arn_string
    import aws_sdk_redshift.types.custom_domain_name_string
    import aws_sdk_redshift.types.integer_optional
    import aws_sdk_redshift.types.string


class DescribeCustomDomainAssociationsMessage(TypedDict):
    custom_domain_name: NotRequired[
        "aws_sdk_redshift.types.custom_domain_name_string.CustomDomainNameString"
    ]
    """<p>The custom domain name for the custom domain association.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "aws_sdk_redshift.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The certificate Amazon Resource Name (ARN) for the custom domain association.</p>"""
    max_records: NotRequired["aws_sdk_redshift.types.integer_optional.IntegerOptional"]
    """<p>The maximum records setting for the associated custom domain.</p>"""
    marker: NotRequired["aws_sdk_redshift.types.string.String"]
    """<p>The marker for the custom domain association.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeCustomDomainAssociationsMessage,
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
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeCustomDomainAssociationsMessage:
    out: DescribeCustomDomainAssociationsMessage = {}  # type: ignore[typeddict-item]
    child_custom_domain_name = el.find("CustomDomainName")
    if child_custom_domain_name is not None:
        out["custom_domain_name"] = str(child_custom_domain_name.text or "")
    child_custom_domain_certificate_arn = el.find("CustomDomainCertificateArn")
    if child_custom_domain_certificate_arn is not None:
        out["custom_domain_certificate_arn"] = str(
            child_custom_domain_certificate_arn.text or ""
        )
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
