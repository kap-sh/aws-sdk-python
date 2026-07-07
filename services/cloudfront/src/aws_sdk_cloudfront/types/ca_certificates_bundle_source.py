"""Generated from Smithy shape ``com.amazonaws.cloudfront#CaCertificatesBundleSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location


class _CaCertificatesBundleSource_CaCertificatesBundleS3Location(
    TypedDict, closed=True
):
    CaCertificatesBundleS3Location: "aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location.CaCertificatesBundleS3Location"


CaCertificatesBundleSource: TypeAlias = (
    _CaCertificatesBundleSource_CaCertificatesBundleS3Location
)


# --- restXml ser/de ---
def serialize_xml(value: CaCertificatesBundleSource, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "CaCertificatesBundleS3Location" in value:
        import aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location

        aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location.serialize_xml(
            value["CaCertificatesBundleS3Location"],
            el,
            "CaCertificatesBundleS3Location",
        )
    else:
        raise SerializationError("CaCertificatesBundleSource: no variant present")


def deserialize_xml(el: Element) -> CaCertificatesBundleSource:
    for child in el:
        if child.tag == "CaCertificatesBundleS3Location":
            import aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location

            return {
                "CaCertificatesBundleS3Location": aws_sdk_cloudfront.types.ca_certificates_bundle_s3_location.deserialize_xml(
                    child
                )
            }
    raise DeserializationError(
        "CaCertificatesBundleSource: no recognized variant element"
    )
