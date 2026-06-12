"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetKeyGroupConfigResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group_config
    import aws_sdk_cloudfront.types.string


class GetKeyGroupConfigResult(TypedDict):
    key_group_config: NotRequired[
        "aws_sdk_cloudfront.types.key_group_config.KeyGroupConfig"
    ]
    """<p>The key group configuration.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The identifier for this version of the key group.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetKeyGroupConfigResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "key_group_config" in value:
        import aws_sdk_cloudfront.types.key_group_config

        aws_sdk_cloudfront.types.key_group_config.serialize_xml(
            value["key_group_config"], el, "KeyGroupConfig"
        )


def deserialize_xml(el: Element) -> GetKeyGroupConfigResult:
    out: GetKeyGroupConfigResult = {}  # type: ignore[typeddict-item]
    child_key_group_config = el.find("KeyGroupConfig")
    if child_key_group_config is not None:
        import aws_sdk_cloudfront.types.key_group_config

        out["key_group_config"] = (
            aws_sdk_cloudfront.types.key_group_config.deserialize_xml(
                child_key_group_config
            )
        )
    return out
