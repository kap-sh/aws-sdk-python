"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetPublicKeyConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.public_key_config
    import aws_sdk_cloudfront.types.string


class GetPublicKeyConfigResult(TypedDict):
    public_key_config: NotRequired[
        "aws_sdk_cloudfront.types.public_key_config.PublicKeyConfig"
    ]
    """<p>A public key configuration.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The identifier for this version of the public key configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetPublicKeyConfigResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "public_key_config" in value:
        import aws_sdk_cloudfront.types.public_key_config

        aws_sdk_cloudfront.types.public_key_config.serialize_xml(
            value["public_key_config"], el, "PublicKeyConfig"
        )


def deserialize_xml(el: Element) -> GetPublicKeyConfigResult:
    out: GetPublicKeyConfigResult = {}  # type: ignore[typeddict-item]
    child_public_key_config = el.find("PublicKeyConfig")
    if child_public_key_config is not None:
        import aws_sdk_cloudfront.types.public_key_config

        out["public_key_config"] = (
            aws_sdk_cloudfront.types.public_key_config.deserialize_xml(
                child_public_key_config
            )
        )
    return out
