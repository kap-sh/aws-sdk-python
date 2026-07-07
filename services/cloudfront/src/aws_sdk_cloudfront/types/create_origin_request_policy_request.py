"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateOriginRequestPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.origin_request_policy_config


class CreateOriginRequestPolicyRequest(TypedDict, closed=True):
    origin_request_policy_config: "aws_sdk_cloudfront.types.origin_request_policy_config.OriginRequestPolicyConfig"
    """<p>An origin request policy configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateOriginRequestPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_cloudfront.types.origin_request_policy_config

    aws_sdk_cloudfront.types.origin_request_policy_config.serialize_xml(
        value["origin_request_policy_config"], el, "OriginRequestPolicyConfig"
    )


def deserialize_xml(el: Element) -> CreateOriginRequestPolicyRequest:
    out: CreateOriginRequestPolicyRequest = {}  # type: ignore[typeddict-item]
    child_origin_request_policy_config = el.find("OriginRequestPolicyConfig")
    if child_origin_request_policy_config is not None:
        import aws_sdk_cloudfront.types.origin_request_policy_config

        out["origin_request_policy_config"] = (
            aws_sdk_cloudfront.types.origin_request_policy_config.deserialize_xml(
                child_origin_request_policy_config
            )
        )
    else:
        raise DeserializationError(
            "CreateOriginRequestPolicyRequest.origin_request_policy_config required"
        )
    return out
