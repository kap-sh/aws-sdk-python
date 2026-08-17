"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.http_body
    import capo_sfn.types.http_headers
    import capo_sfn.types.http_method
    import capo_sfn.types.http_protocol
    import capo_sfn.types.url


class InspectionDataRequest(TypedDict, closed=True):
    protocol: NotRequired["capo_sfn.types.http_protocol.HTTPProtocol"]
    """<p>The protocol used to make the HTTP request.</p>"""
    method: NotRequired["capo_sfn.types.http_method.HTTPMethod"]
    """<p>The HTTP method used for the HTTP request.</p>"""
    url: NotRequired["capo_sfn.types.url.URL"]
    """<p>The API endpoint used for the HTTP request.</p>"""
    headers: NotRequired["capo_sfn.types.http_headers.HTTPHeaders"]
    """<p>The request headers associated with the HTTP request.</p>"""
    body: NotRequired["capo_sfn.types.http_body.HTTPBody"]
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
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("method") is not None:
        out["method"] = data["method"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("headers") is not None:
        out["headers"] = data["headers"]
    if data.get("body") is not None:
        out["body"] = data["body"]
    return out
