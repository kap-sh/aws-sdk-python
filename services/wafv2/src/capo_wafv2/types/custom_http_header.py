"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomHTTPHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.custom_http_header_name
    import capo_wafv2.types.custom_http_header_value


class CustomHTTPHeader(TypedDict, closed=True):
    name: "capo_wafv2.types.custom_http_header_name.CustomHTTPHeaderName"
    """<p>The name of the custom header. </p> <p>For custom request header insertion, when WAF inserts the header into the request, it prefixes this name <code>x-amzn-waf-</code>, to avoid confusion with the headers that are already in the request. For example, for the header name <code>sample</code>, WAF inserts the header <code>x-amzn-waf-sample</code>.</p>"""
    value: "capo_wafv2.types.custom_http_header_value.CustomHTTPHeaderValue"
    """<p>The value of the custom header.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomHTTPHeader) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomHTTPHeader:
    out: CustomHTTPHeader = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CustomHTTPHeader.name required")
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        raise DeserializationError("CustomHTTPHeader.value required")
    return out
