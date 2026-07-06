"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sfn.types.http_body
    import aws_sdk_sfn.types.http_headers
    import aws_sdk_sfn.types.http_method
    import aws_sdk_sfn.types.http_protocol
    import aws_sdk_sfn.types.url


class InspectionDataRequest(TypedDict, closed=True):
    protocol: NotRequired["aws_sdk_sfn.types.http_protocol.HTTPProtocol"]
    """<p>The protocol used to make the HTTP request.</p>"""
    method: NotRequired["aws_sdk_sfn.types.http_method.HTTPMethod"]
    """<p>The HTTP method used for the HTTP request.</p>"""
    url: NotRequired["aws_sdk_sfn.types.url.URL"]
    """<p>The API endpoint used for the HTTP request.</p>"""
    headers: NotRequired["aws_sdk_sfn.types.http_headers.HTTPHeaders"]
    """<p>The request headers associated with the HTTP request.</p>"""
    body: NotRequired["aws_sdk_sfn.types.http_body.HTTPBody"]
    """<p>The request body for the HTTP request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionDataRequest) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "method" in value:
        out["method"] = value["method"]
    if "url" in value:
        out["url"] = value["url"]
    if "headers" in value:
        out["headers"] = value["headers"]
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionDataRequest:
    out: InspectionDataRequest = {}  # type: ignore[typeddict-item]
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "method" in data:
        out["method"] = data["method"]
    if "url" in data:
        out["url"] = data["url"]
    if "headers" in data:
        out["headers"] = data["headers"]
    if "body" in data:
        out["body"] = data["body"]
    return out
