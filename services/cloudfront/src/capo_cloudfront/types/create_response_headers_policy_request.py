"""Generated from Smithy shape ``com.amazonaws.cloudfront#CreateResponseHeadersPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement
from capo_cloudfront.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudfront.types.response_headers_policy_config


class CreateResponseHeadersPolicyRequest(TypedDict, closed=True):
    response_headers_policy_config: "capo_cloudfront.types.response_headers_policy_config.ResponseHeadersPolicyConfig"
    """<p>Contains metadata about the response headers policy, and a set of configurations that specify the HTTP headers.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateResponseHeadersPolicyRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.response_headers_policy_config

    capo_cloudfront.types.response_headers_policy_config.serialize_xml(
        value["response_headers_policy_config"], el, "ResponseHeadersPolicyConfig"
    )


def deserialize_xml(el: Element) -> CreateResponseHeadersPolicyRequest:
    out: CreateResponseHeadersPolicyRequest = {}  # type: ignore[typeddict-item]
    child_response_headers_policy_config = el.find("ResponseHeadersPolicyConfig")
    if child_response_headers_policy_config is not None:
        import capo_cloudfront.types.response_headers_policy_config

        out["response_headers_policy_config"] = (
            capo_cloudfront.types.response_headers_policy_config.deserialize_xml(
                child_response_headers_policy_config
            )
        )
    else:
        raise DeserializationError(
            "CreateResponseHeadersPolicyRequest.response_headers_policy_config required"
        )
    return out
