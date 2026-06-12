"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginAccessControlRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_access_control_config


class CreateOriginAccessControlRequest(TypedDict):
    origin_access_control_config: "aws_sdk_cloudfront.types.origin_access_control_config.OriginAccessControlConfig"
    """<p>Contains the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateOriginAccessControlRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.origin_access_control_config

    aws_sdk_cloudfront.types.origin_access_control_config.serialize_xml(
        value["origin_access_control_config"], el, "OriginAccessControlConfig"
    )


def deserialize_xml(el: Element) -> CreateOriginAccessControlRequest:
    out: CreateOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
    child_origin_access_control_config = el.find("OriginAccessControlConfig")
    if child_origin_access_control_config is not None:
        import aws_sdk_cloudfront.types.origin_access_control_config

        out["origin_access_control_config"] = (
            aws_sdk_cloudfront.types.origin_access_control_config.deserialize_xml(
                child_origin_access_control_config
            )
        )
    else:
        raise DeserializationError(
            "CreateOriginAccessControlRequest.origin_access_control_config required"
        )
    return out
