"""Generated from Smithy shape ``com.amazonaws.cloudfront#UpdateOriginAccessControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_access_control_config
    import aws_sdk_cloudfront.types.string


class UpdateOriginAccessControlRequest(TypedDict, closed=True):
    origin_access_control_config: "aws_sdk_cloudfront.types.origin_access_control_config.OriginAccessControlConfig"
    """<p>An origin access control.</p>"""
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The unique identifier of the origin access control that you are updating.</p>"""
    if_match: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version (<code>ETag</code> value) of the origin access control that you are updating.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: UpdateOriginAccessControlRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.origin_access_control_config

    aws_sdk_cloudfront.types.origin_access_control_config.serialize_xml(
        value["origin_access_control_config"], el, "OriginAccessControlConfig"
    )


def deserialize_xml(el: Element) -> UpdateOriginAccessControlRequest:
    out: UpdateOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
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
            "UpdateOriginAccessControlRequest.origin_access_control_config required"
        )
    return out
