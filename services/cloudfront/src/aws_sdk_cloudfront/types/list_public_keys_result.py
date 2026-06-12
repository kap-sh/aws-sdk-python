"""Generated from Smithy shape ``com.amazonaws.cloudfront#ListPublicKeysResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.public_key_list


class ListPublicKeysResult(TypedDict):
    public_key_list: NotRequired[
        "aws_sdk_cloudfront.types.public_key_list.PublicKeyList"
    ]
    """<p>Returns a list of all public keys that have been added to CloudFront for this account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ListPublicKeysResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_key_list" in value:
        import aws_sdk_cloudfront.types.public_key_list

        aws_sdk_cloudfront.types.public_key_list.serialize_xml(
            value["public_key_list"], el, "PublicKeyList"
        )


def deserialize_xml(el: Element) -> ListPublicKeysResult:
    out: ListPublicKeysResult = {}  # type: ignore[typeddict-item]
    child_public_key_list = el.find("PublicKeyList")
    if child_public_key_list is not None:
        import aws_sdk_cloudfront.types.public_key_list

        out["public_key_list"] = (
            aws_sdk_cloudfront.types.public_key_list.deserialize_xml(
                child_public_key_list
            )
        )
    return out
