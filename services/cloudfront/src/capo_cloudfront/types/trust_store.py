"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.boolean
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.trust_store_status


class TrustStore(TypedDict, closed=True):
    id: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The trust store's ID.</p>"""
    arn: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The trust store's Amazon Resource Name (ARN).</p>"""
    name: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The trust store's name.</p>"""
    status: NotRequired["capo_cloudfront.types.trust_store_status.TrustStoreStatus"]
    """<p>The trust store's status.</p>"""
    number_of_ca_certificates: NotRequired["capo_cloudfront.types.integer.integer"]
    """<p>The trust store's number of CA certificates.</p>"""
    last_modified_time: NotRequired["capo_cloudfront.types.timestamp.timestamp"]
    """<p>The trust store's last modified time.</p>"""
    reason: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The trust store's reason.</p>"""
    use_client_certificate_ocsp_endpoint: NotRequired[
        "capo_cloudfront.types.boolean.boolean"
    ]
    """<p>A Boolean that determines whether the trust store uses the CA certificate's OCSP endpoint to check certificate revocation status.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrustStore, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "id" in value:
        SubElement(el, "Id").text = str(value["id"])
    if "arn" in value:
        SubElement(el, "Arn").text = str(value["arn"])
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "status" in value:
        import capo_cloudfront.types.trust_store_status

        capo_cloudfront.types.trust_store_status.serialize_xml(
            value["status"], el, "Status"
        )
    if "number_of_ca_certificates" in value:
        SubElement(el, "NumberOfCaCertificates").text = str(
            value["number_of_ca_certificates"]
        )
    if "last_modified_time" in value:
        import capo_cloudfront.types.timestamp

        capo_cloudfront.types.timestamp.serialize_xml(
            value["last_modified_time"], el, "LastModifiedTime"
        )
    if "reason" in value:
        SubElement(el, "Reason").text = str(value["reason"])
    if "use_client_certificate_ocsp_endpoint" in value:
        SubElement(el, "UseClientCertificateOCSPEndpoint").text = (
            "true" if value["use_client_certificate_ocsp_endpoint"] else "false"
        )


def deserialize_xml(el: Element) -> TrustStore:
    out: TrustStore = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudfront.types.trust_store_status

        out["status"] = capo_cloudfront.types.trust_store_status.deserialize_xml(
            child_status
        )
    child_number_of_ca_certificates = el.find("NumberOfCaCertificates")
    if child_number_of_ca_certificates is not None:
        out["number_of_ca_certificates"] = int(
            child_number_of_ca_certificates.text or ""
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_use_client_certificate_ocsp_endpoint = el.find(
        "UseClientCertificateOCSPEndpoint"
    )
    if child_use_client_certificate_ocsp_endpoint is not None:
        out["use_client_certificate_ocsp_endpoint"] = (
            child_use_client_certificate_ocsp_endpoint.text or ""
        ).lower() == "true"
    return out
