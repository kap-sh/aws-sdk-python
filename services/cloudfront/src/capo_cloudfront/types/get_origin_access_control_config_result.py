"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginAccessControlConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.origin_access_control_config
    import capo_cloudfront.types.string


class GetOriginAccessControlConfigResult(TypedDict, closed=True):
    origin_access_control_config: NotRequired[
        "capo_cloudfront.types.origin_access_control_config.OriginAccessControlConfig"
    ]
    """<p>Contains an origin access control configuration.</p>"""
    e_tag: NotRequired["capo_cloudfront.types.string.string"]
    """<p>The version identifier for the current version of the origin access control.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginAccessControlConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_access_control_config" in value:
        import capo_cloudfront.types.origin_access_control_config

        capo_cloudfront.types.origin_access_control_config.serialize_xml(
            value["origin_access_control_config"], el, "OriginAccessControlConfig"
        )


def deserialize_xml(el: Element) -> GetOriginAccessControlConfigResult:
    out: GetOriginAccessControlConfigResult = {}  # type: ignore[typeddict-item]
    child_origin_access_control_config = el.find("OriginAccessControlConfig")
    if child_origin_access_control_config is not None:
        import capo_cloudfront.types.origin_access_control_config

        out["origin_access_control_config"] = (
            capo_cloudfront.types.origin_access_control_config.deserialize_xml(
                child_origin_access_control_config
            )
        )
    return out
