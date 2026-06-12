"""Generated from Smithy shape ``com.amazonaws.cloudfront#ResponseHeadersPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudfront._protocol.xml import Element, SubElement
from aws_sdk_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudfront.types.response_headers_policy_config
    import aws_sdk_cloudfront.types.string
    import aws_sdk_cloudfront.types.timestamp


class ResponseHeadersPolicy(TypedDict):
    id: "aws_sdk_cloudfront.types.string.string"
    """<p>The identifier for the response headers policy.</p>"""
    last_modified_time: "aws_sdk_cloudfront.types.timestamp.timestamp"
    """<p>The date and time when the response headers policy was last modified.</p>"""
    response_headers_policy_config: "aws_sdk_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig"
    """<p>A response headers policy configuration.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ResponseHeadersPolicy, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Id").text = str(value["id"])
    import aws_sdk_cloudfront.types.timestamp

    aws_sdk_cloudfront.types.timestamp.serialize_xml(
        value["last_modified_time"], el, "LastModifiedTime"
    )
    import aws_sdk_cloudfront.types.response_headers_policy_config

    aws_sdk_cloudfront.types.response_headers_policy_config.serialize_xml(
        value["response_headers_policy_config"], el, "ResponseHeadersPolicyConfig"
    )


def deserialize_xml(el: Element) -> ResponseHeadersPolicy:
    out: ResponseHeadersPolicy = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    else:
        raise DeserializationError("ResponseHeadersPolicy.id required")
    child_last_modified_time = el.find("LastModifiedTime")
    if child_last_modified_time is not None:
        import aws_sdk_cloudfront.types.timestamp

        out["last_modified_time"] = aws_sdk_cloudfront.types.timestamp.deserialize_xml(
            child_last_modified_time
        )
    else:
        raise DeserializationError("ResponseHeadersPolicy.last_modified_time required")
    child_response_headers_policy_config = el.find("ResponseHeadersPolicyConfig")
    if child_response_headers_policy_config is not None:
        import aws_sdk_cloudfront.types.response_headers_policy_config

        out["response_headers_policy_config"] = (
            aws_sdk_cloudfront.types.response_headers_policy_config.deserialize_xml(
                child_response_headers_policy_config
            )
        )
    else:
        raise DeserializationError(
            "ResponseHeadersPolicy.response_headers_policy_config required"
        )
    return out
