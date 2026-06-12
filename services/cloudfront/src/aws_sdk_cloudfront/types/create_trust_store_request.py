"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateTrustStoreRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.boolean
    import aws_sdk_cloudfront.types.ca_certificates_bundle_source
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.tags


class CreateTrustStoreRequest(TypedDict):
    name: "aws_sdk_cloudfront.types.string.string"
    """<p>A name for the trust store.</p>"""
    ca_certificates_bundle_source: "aws_sdk_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource"
    """<p>The CA certificates bundle source for the trust store.</p>"""
    use_client_certificate_ocsp_endpoint: NotRequired[
        "aws_sdk_cloudfront.types.boolean.boolean"
    ]
    """<p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>"""
    tags: NotRequired["aws_sdk_cloudfront.types.tags.Tags"]


# --- restXml ser/de ---
def serialize_xml(value: CreateTrustStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_cloudfront.types.ca_certificates_bundle_source

    aws_sdk_cloudfront.types.ca_certificates_bundle_source.serialize_xml(
        value["ca_certificates_bundle_source"], el, "CaCertificatesBundleSource"
    )
    if "use_client_certificate_ocsp_endpoint" in value:
        SubElement(el, "UseClientCertificateOCSPEndpoint").text = (
            "true" if value["use_client_certificate_ocsp_endpoint"] else "false"
        )
    if "tags" in value:
        import aws_sdk_cloudfront.types.tags

        aws_sdk_cloudfront.types.tags.serialize_xml(value["tags"], el, "Tags")


def deserialize_xml(el: Element) -> CreateTrustStoreRequest:
    out: CreateTrustStoreRequest = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateTrustStoreRequest.name required")
    child_ca_certificates_bundle_source = el.find("CaCertificatesBundleSource")
    if child_ca_certificates_bundle_source is not None:
        import aws_sdk_cloudfront.types.ca_certificates_bundle_source

        out["ca_certificates_bundle_source"] = (
            aws_sdk_cloudfront.types.ca_certificates_bundle_source.deserialize_xml(
                child_ca_certificates_bundle_source
            )
        )
    else:
        raise DeserializationError(
            "CreateTrustStoreRequest.ca_certificates_bundle_source required"
        )
    child_use_client_certificate_ocsp_endpoint = el.find(
        "UseClientCertificateOCSPEndpoint"
    )
    if child_use_client_certificate_ocsp_endpoint is not None:
        out["use_client_certificate_ocsp_endpoint"] = (
            child_use_client_certificate_ocsp_endpoint.text or ""
        ).lower() == "true"
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_cloudfront.types.tags

        out["tags"] = aws_sdk_cloudfront.types.tags.deserialize_xml(child_tags)
    return out
