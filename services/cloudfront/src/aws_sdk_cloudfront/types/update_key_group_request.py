"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateKeyGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group_config
    import aws_sdk_cloudfront.types.string


class UpdateKeyGroupRequest(TypedDict):
    key_group_config: "aws_sdk_cloudfront.types.key_group_config.KeyGroupConfig"
    """<p>The key group configuration.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier of the key group that you are updating.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The version of the key group that you are updating. The version is the key group's <code>ETag</code> value.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: UpdateKeyGroupRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.key_group_config

    aws_sdk_cloudfront.types.key_group_config.serialize_xml(
        value["key_group_config"], el, "KeyGroupConfig"
    )


def deserialize_xml(el: Element) -> UpdateKeyGroupRequest:
    out: UpdateKeyGroupRequest = {}  # type: ignore[typeddict-item]
    child_key_group_config = el.find("KeyGroupConfig")
    if child_key_group_config is not None:
        import aws_sdk_cloudfront.types.key_group_config

        out["key_group_config"] = (
            aws_sdk_cloudfront.types.key_group_config.deserialize_xml(
                child_key_group_config
            )
        )
    else:
        raise DeserializationError("UpdateKeyGroupRequest.key_group_config required")
    return out
