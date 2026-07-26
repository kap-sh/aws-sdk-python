"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateTrustStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.ca_certificates_bundle_source
    import capo_cloudfront.types.resource_id
    import capo_cloudfront.types.string


class UpdateTrustStoreRequest(TypedDict, closed=True):
    id: "capo_cloudfront.types.resource_id.ResourceId"
    """<p>The trust store ID.</p>"""
    ca_certificates_bundle_source: NotRequired[
        "capo_cloudfront.types.ca_certificates_bundle_source.CaCertificatesBundleSource"
    ]
    """<p>The CA certificates bundle source.</p>"""
    use_client_certificate_ocsp_endpoint: NotRequired[
        "capo_cloudfront.types.boolean.boolean"
    ]
    """<p>A Boolean that determines whether to use the CA certificate's OCSP endpoint to check certificate revocation status.</p>"""
    if_match: "capo_cloudfront.types.string.string"
    """<p>The current version (<code>ETag</code> value) of the trust store you are updating.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateTrustStoreRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "ca_certificates_bundle_source" in value:
        import capo_cloudfront.types.ca_certificates_bundle_source

        capo_cloudfront.types.ca_certificates_bundle_source.serialize_xml(
            value["ca_certificates_bundle_source"], el, "CaCertificatesBundleSource"
        )


def deserialize_xml(el: Element) -> UpdateTrustStoreRequest:
    out: UpdateTrustStoreRequest = {}  # type: ignore[typeddict-item]
    child_ca_certificates_bundle_source = el.find("CaCertificatesBundleSource")
    if child_ca_certificates_bundle_source is not None:
        import capo_cloudfront.types.ca_certificates_bundle_source

        out["ca_certificates_bundle_source"] = (
            capo_cloudfront.types.ca_certificates_bundle_source.deserialize_xml(
                child_ca_certificates_bundle_source
            )
        )
    return out
