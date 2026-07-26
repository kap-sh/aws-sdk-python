"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdatePublicKeyResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key
    import capo_cloudfront.types.string


class UpdatePublicKeyResult(TypedDict, closed=True):
    public_key: NotRequired["capo_cloudfront.types.public_key.PublicKey"]
    """<p>The public key.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The identifier of the current version of the public key.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdatePublicKeyResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_key" in value:
        import capo_cloudfront.types.public_key

        capo_cloudfront.types.public_key.serialize_xml(
            value["public_key"], el, "PublicKey"
        )


def deserialize_xml(el: Element) -> UpdatePublicKeyResult:
    out: UpdatePublicKeyResult = {}  # type: ignore[typeddict-item]
    child_public_key = el.find("PublicKey")
    if child_public_key is not None:
        import capo_cloudfront.types.public_key

        out["public_key"] = capo_cloudfront.types.public_key.deserialize_xml(
            child_public_key
        )
    return out
