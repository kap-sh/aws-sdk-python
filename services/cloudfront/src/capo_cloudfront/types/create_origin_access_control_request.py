"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginAccessControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_config


class CreateOriginAccessControlRequest(TypedDict, closed=True):
    origin_access_control_config: (
        "capo_cloudfront.types.origin_access_control_config.OriginAccessControlConfig"
    )
    """<p>Contains the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateOriginAccessControlRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.origin_access_control_config

    capo_cloudfront.types.origin_access_control_config.serialize_xml(
        value["origin_access_control_config"], el, "OriginAccessControlConfig"
    )


def deserialize_xml(el: Element) -> CreateOriginAccessControlRequest:
    out: CreateOriginAccessControlRequest = {}  # type: ignore[typeddict-item]
    child_origin_access_control_config = el.find("OriginAccessControlConfig")
    if child_origin_access_control_config is not None:
        import capo_cloudfront.types.origin_access_control_config

        out["origin_access_control_config"] = (
            capo_cloudfront.types.origin_access_control_config.deserialize_xml(
                child_origin_access_control_config
            )
        )
    else:
        raise DeserializationError(
            "CreateOriginAccessControlRequest.origin_access_control_config required"
        )
    return out
