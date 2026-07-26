"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreatePublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.public_key_config


class CreatePublicKeyRequest(TypedDict, closed=True):
    public_key_config: "capo_cloudfront.types.public_key_config.PublicKeyConfig"
    """<p>A CloudFront public key configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreatePublicKeyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.public_key_config

    capo_cloudfront.types.public_key_config.serialize_xml(
        value["public_key_config"], el, "PublicKeyConfig"
    )


def deserialize_xml(el: Element) -> CreatePublicKeyRequest:
    out: CreatePublicKeyRequest = {}  # type: ignore[typeddict-item]
    child_public_key_config = el.find("PublicKeyConfig")
    if child_public_key_config is not None:
        import capo_cloudfront.types.public_key_config

        out["public_key_config"] = (
            capo_cloudfront.types.public_key_config.deserialize_xml(
                child_public_key_config
            )
        )
    else:
        raise DeserializationError("CreatePublicKeyRequest.public_key_config required")
    return out
