"""Generated from Smithy shape ``com.amazonaws.cloudfront#TrustStoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.integer
    import capo_cloudfront.types.string
    import capo_cloudfront.types.timestamp
    import capo_cloudfront.types.trust_store_status


class TrustStoreSummary(TypedDict, closed=True):
    id: "capo_cloudfront.types.string.string"
    """<p>The trust store's ID.</p>"""
    arn: "capo_cloudfront.types.string.string"
    """<p>The trust store's Amazon Resource Name (ARN).</p>"""
    name: "capo_cloudfront.types.string.string"
    """<p>The trust store's name.</p>"""
    status: "capo_cloudfront.types.trust_store_status.TrustStoreStatus"
    """<p>The trust store's status.</p>"""
    number_of_ca_certificates: "capo_cloudfront.types.integer.integer"
    """<p>The trust store's number of CA certificates.</p>"""
    last_modified_time: "capo_cloudfront.types.timestamp.timestamp"
    """<p>The trust store's last modified time.</p>"""
    reason: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The trust store's reason.</p>"""
    e_tag: "capo_cloudfront.types.string.string"
    """<p>The version identifier for the current version of the trust store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: TrustStoreSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    SubElement(el, "Arn").text = str(value["arn"])
    SubElement(el, "Name").text = str(value["name"])
    import capo_cloudfront.types.trust_store_status

    capo_cloudfront.types.trust_store_status.serialize_xml(
        value["status"], el, "Status"
    )
    SubElement(el, "NumberOfCaCertificates").text = str(
        value["number_of_ca_certificates"]
    )
    import capo_cloudfront.types.timestamp

    capo_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    if "reason" in value:
        SubElement(el, "Reason").text = str(value["reason"])
    SubElement(el, "ETag").text = str(value["e_tag"])


def deserialize_xml(el: Element) -> TrustStoreSummary:
    out: TrustStoreSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("TrustStoreSummary.id required")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    else:
        raise DeserializationError("TrustStoreSummary.arn required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("TrustStoreSummary.name required")
    child_status = el.find("Status")
    if child_status is not None:
        import capo_cloudfront.types.trust_store_status

        out["status"] = capo_cloudfront.types.trust_store_status.deserialize_xml(
            child_status
        )
    else:
        raise DeserializationError("TrustStoreSummary.status required")
    child_number_of_ca_certificates = el.find("NumberOfCaCertificates")
    if child_number_of_ca_certificates is not None:
        out["number_of_ca_certificates"] = int(
            child_number_of_ca_certificates.text or ""
        )
    else:
        raise DeserializationError(
            "TrustStoreSummary.number_of_ca_certificates required"
        )
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import capo_cloudfront.types.timestamp

        out["last_modified_time"] = capo_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("TrustStoreSummary.last_modified_time required")
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    else:
        raise DeserializationError("TrustStoreSummary.e_tag required")
    return out
