"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreatePublicKeyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.public_key_config


class CreatePublicKeyRequest(TypedDict):
    public_key_config: "aws_sdk_cloudfront.types.public_key_config.PublicKeyConfig"
    """<p>A CloudFront public key configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreatePublicKeyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.public_key_config

    aws_sdk_cloudfront.types.public_key_config.serialize_xml(
        value["public_key_config"], el, "PublicKeyConfig"
    )


def deserialize_xml(el: Element) -> CreatePublicKeyRequest:
    out: CreatePublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_public_key_config = el.find("PublicKeyConfig")
    if child_public_key_config is not None:
        import aws_sdk_cloudfront.types.public_key_config

        out["public_key_config"] = (
            aws_sdk_cloudfront.types.public_key_config.deserialize_xml(
                child_public_key_config
            )
        )
    else:
        raise DeserializationError("CreatePublicKeyRequest.public_key_config required")
    return out
