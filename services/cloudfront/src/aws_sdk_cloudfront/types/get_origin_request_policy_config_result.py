"""Generated from Smithy shape ``com.amazonaws.cloudfront#GetOriginRequestPolicyConfigResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_request_policy_config
    import aws_sdk_cloudfront.types.string


class GetOriginRequestPolicyConfigResult(TypedDict, closed=True):
    origin_request_policy_config: NotRequired[
        "aws_sdk_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig"
    ]
    """<p>The origin request policy configuration.</p>"""
    e_tag: NotRequired["aws_sdk_cloudfront.types.string.string"]
    """<p>The current version of the origin request policy.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetOriginRequestPolicyConfigResult, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "origin_request_policy_config" in value:
        import aws_sdk_cloudfront.types.origin_request_policy_config

        aws_sdk_cloudfront.types.origin_request_policy_config.serialize_xml(
            value["origin_request_policy_config"], el, "OriginRequestPolicyConfig"
        )


def deserialize_xml(el: Element) -> GetOriginRequestPolicyConfigResult:
    out: GetOriginRequestPolicyConfigResult = {}  # type: ignore[typeddict-item]
    child_origin_request_policy_config = el.find("OriginRequestPolicyConfig")
    if child_origin_request_policy_config is not None:
        import aws_sdk_cloudfront.types.origin_request_policy_config

        out["origin_request_policy_config"] = (
            aws_sdk_cloudfront.types.origin_request_policy_config.deserialize_xml(
                child_origin_request_policy_config
            )
        )
    return out
