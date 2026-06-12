"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdatePublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.public_key_config
    import aws_sdk_cloudfront.types.string


class UpdatePublicKeyRequest(TypedDict):
    public_key_config: "aws_sdk_cloudfront.types.public_key_config.PublicKeyConfig"
    """<p>A public key configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the public key that you are updating.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The value of the <code>ETag</code> header that you received when retrieving the public key to update. For example: <code>E2QWRUHAPOMQZL</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdatePublicKeyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.public_key_config

    aws_sdk_cloudfront.types.public_key_config.serialize_xml(
        value["public_key_config"], el, "PublicKeyConfig"
    )


def deserialize_xml(el: Element) -> UpdatePublicKeyRequest:
    out: UpdatePublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_public_key_config = el.find("PublicKeyConfig")
    if child_public_key_config is not None:
        import aws_sdk_cloudfront.types.public_key_config

        out["public_key_config"] = (
            aws_sdk_cloudfront.types.public_key_config.deserialize_xml(
                child_public_key_config
            )
        )
    else:
        raise DeserializationError("UpdatePublicKeyRequest.public_key_config required")
    return out
