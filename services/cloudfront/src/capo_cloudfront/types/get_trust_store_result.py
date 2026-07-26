"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetTrustStoreResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.string
    import capo_cloudfront.types.trust_store


class GetTrustStoreResult(TypedDict, closed=True):
    trust_store: NotRequired["capo_cloudfront.types.trust_store.TrustStore"]
    """<p>The trust store.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the trust store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetTrustStoreResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "trust_store" in value:
        import capo_cloudfront.types.trust_store

        capo_cloudfront.types.trust_store.serialize_xml(
            value["trust_store"], el, "TrustStore"
        )


def deserialize_xml(el: Element) -> GetTrustStoreResult:
    out: GetTrustStoreResult = {}  # type: ignore[typeddict-item]
    child_trust_store = el.find("TrustStore")
    if child_trust_store is not None:
        import capo_cloudfront.types.trust_store

        out["trust_store"] = capo_cloudfront.types.trust_store.deserialize_xml(
            child_trust_store
        )
    return out
