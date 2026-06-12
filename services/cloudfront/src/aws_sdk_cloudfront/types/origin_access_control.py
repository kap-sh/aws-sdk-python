"""Generated from Smithy shape ``com.amazonaws.cloudfront#OriginAccessControl``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_access_control_config
    import aws_sdk_cloudfront.types.string


class OriginAccessControl(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control.</p>"""
    origin_access_control_config: NotRequired[
        "aws_sdk_cloudfront.types.origin_access_control_config.OriginAccessControlConfig"
    ]
    """<p>The origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: OriginAccessControl, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    if "origin_access_control_config" in value:
        import aws_sdk_cloudfront.types.origin_access_control_config

        aws_sdk_cloudfront.types.origin_access_control_config.serialize_xml(
            value["origin_access_control_config"], el, "OriginAccessControlConfig"
        )


def deserialize_xml(el: Element) -> OriginAccessControl:
    out: OriginAccessControl = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("OriginAccessControl.id required")
    child_origin_access_control_config = el.find("OriginAccessControlConfig")
    if child_origin_access_control_config is not None:
        import aws_sdk_cloudfront.types.origin_access_control_config

        out["origin_access_control_config"] = (
            aws_sdk_cloudfront.types.origin_access_control_config.deserialize_xml(
                child_origin_access_control_config
            )
        )
    return out
