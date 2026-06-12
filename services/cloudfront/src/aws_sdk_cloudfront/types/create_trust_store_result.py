"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateTrustStoreResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.trust_store


class CreateTrustStoreResult(TypedDict):
    trust_store: NotRequired["aws_sdk_cloudfront.types.trust_store.TrustStore"]
    """<p>The trust store.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the trust store.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateTrustStoreResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "trust_store" in value:
        import aws_sdk_cloudfront.types.trust_store

        aws_sdk_cloudfront.types.trust_store.serialize_xml(
            value["trust_store"], el, "TrustStore"
        )


def deserialize_xml(el: Element) -> CreateTrustStoreResult:
    out: CreateTrustStoreResult = {}  # type: ignore[typeddict-item]
    child_trust_store = el.find("TrustStore")
    if child_trust_store is not None:
        import aws_sdk_cloudfront.types.trust_store

        out["trust_store"] = aws_sdk_cloudfront.types.trust_store.deserialize_xml(
            child_trust_store
        )
    return out
