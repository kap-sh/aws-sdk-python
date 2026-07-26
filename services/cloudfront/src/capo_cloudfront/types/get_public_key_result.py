"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetPublicKeyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key
    import capo_cloudfront.types.string


class GetPublicKeyResult(TypedDict, closed=True):
    public_key: NotRequired["capo_cloudfront.types.public_key.PublicKey"]
    """<p>The public key.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The identifier for this version of the public key.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetPublicKeyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_key" in value:
        import capo_cloudfront.types.public_key

        capo_cloudfront.types.public_key.serialize_xml(
            value["public_key"], el, "PublicKey"
        )


def deserialize_xml(el: Element) -> GetPublicKeyResult:
    out: GetPublicKeyResult = {}  # type: ignore[typeddict-item]
    child_public_key = el.find("PublicKey")
    if child_public_key is not None:
        import capo_cloudfront.types.public_key

        out["public_key"] = capo_cloudfront.types.public_key.deserialize_xml(
            child_public_key
        )
    return out
