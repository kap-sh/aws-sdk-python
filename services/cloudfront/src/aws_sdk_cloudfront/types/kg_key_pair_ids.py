"""Generated from Smithy shape ``com.amazonaws.cloudfront#KGKeyPairIds``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_pair_ids
    import aws_sdk_cloudfront.types.string


class KGKeyPairIds(TypedDict, closed=True):
    key_group_id: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The identifier of the key group that contains the public keys.</p>"""
    key_pair_ids: NotRequired["aws_sdk_cloudfront.types.key_pair_ids.KeyPairIds"]


# --- restXml ser/de ---
def serialize_xml(value: KGKeyPairIds, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group_id" in value:
        SubElement(el, "KeyGroupId").text = str(value["key_group_id"])
    if "key_pair_ids" in value:
        import aws_sdk_cloudfront.types.key_pair_ids

        aws_sdk_cloudfront.types.key_pair_ids.serialize_xml(
            value["key_pair_ids"], el, "KeyPairIds"
        )


def deserialize_xml(el: Element) -> KGKeyPairIds:
    out: KGKeyPairIds = {}  # type: ignore[typeddict-item]
    child_key_group_id = el.find("KeyGroupId")
    if child_key_group_id is not None:
        out["key_group_id"] = str(child_key_group_id.text or "")
    child_key_pair_ids = el.find("KeyPairIds")
    if child_key_pair_ids is not None:
        import aws_sdk_cloudfront.types.key_pair_ids

        out["key_pair_ids"] = aws_sdk_cloudfront.types.key_pair_ids.deserialize_xml(
            child_key_pair_ids
        )
    return out
