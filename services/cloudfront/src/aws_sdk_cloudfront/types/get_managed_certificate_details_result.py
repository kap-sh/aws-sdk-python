"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetManagedCertificateDetailsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.managed_certificate_details


class GetManagedCertificateDetailsResult(TypedDict, closed=True):
    managed_certificate_details: NotRequired[
        "aws_sdk_cloudfront.types.managed_certificate_details.ManagedCertificateDetails"
    ]
    """<p>Contains details about the CloudFront managed ACM certificate.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetManagedCertificateDetailsResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "managed_certificate_details" in value:
        import aws_sdk_cloudfront.types.managed_certificate_details

        aws_sdk_cloudfront.types.managed_certificate_details.serialize_xml(
            value["managed_certificate_details"], el, "ManagedCertificateDetails"
        )


def deserialize_xml(el: Element) -> GetManagedCertificateDetailsResult:
    out: GetManagedCertificateDetailsResult = {}  # type: ignore[typeddict-item]
    child_managed_certificate_details = el.find("ManagedCertificateDetails")
    if child_managed_certificate_details is not None:
        import aws_sdk_cloudfront.types.managed_certificate_details

        out["managed_certificate_details"] = (
            aws_sdk_cloudfront.types.managed_certificate_details.deserialize_xml(
                child_managed_certificate_details
            )
        )
    return out
