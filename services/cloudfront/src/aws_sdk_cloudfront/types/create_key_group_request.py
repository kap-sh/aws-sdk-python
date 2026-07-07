"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateKeyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.key_group_config


class CreateKeyGroupRequest(TypedDict, closed=True):
    key_group_config: "aws_sdk_cloudfront.types.key_group_config.KeyGroupConfig"
    """<p>A key group configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateKeyGroupRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.key_group_config

    aws_sdk_cloudfront.types.key_group_config.serialize_xml(
        value["key_group_config"], el, "KeyGroupConfig"
    )


def deserialize_xml(el: Element) -> CreateKeyGroupRequest:
    out: CreateKeyGroupRequest = {}  # type: ignore[typeddict-item]
    child_key_group_config = el.find("KeyGroupConfig")
    if child_key_group_config is not None:
        import aws_sdk_cloudfront.types.key_group_config

        out["key_group_config"] = (
            aws_sdk_cloudfront.types.key_group_config.deserialize_xml(
                child_key_group_config
            )
        )
    else:
        raise DeserializationError("CreateKeyGroupRequest.key_group_config required")
    return out
