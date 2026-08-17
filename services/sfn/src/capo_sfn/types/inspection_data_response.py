"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionDataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.http_body
    import capo_sfn.types.http_headers
    import capo_sfn.types.http_protocol
    import capo_sfn.types.http_status_code
    import capo_sfn.types.http_status_message


class InspectionDataResponse(TypedDict, closed=True):
    protocol: NotRequired["capo_sfn.types.http_protocol.HTTPProtocol"]
    """<p>The protocol used to return the HTTP response.</p>"""
    status_code: NotRequired["capo_sfn.types.http_status_code.HTTPStatusCode"]
    """<p>The HTTP response status code for the HTTP response.</p>"""
    status_message: NotRequired["capo_sfn.types.http_status_message.HTTPStatusMessage"]
    """<p>The message associated with the HTTP status code.</p>"""
    headers: NotRequired["capo_sfn.types.http_headers.HTTPHeaders"]
    """<p>The response headers associated with the HTTP response.</p>"""
    body: NotRequired["capo_sfn.types.http_body.HTTPBody"]
    """<p>The HTTP response returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionDataResponse) -> dict:
    out: dict = {}
    if "protocol" in value:
        out["protocol"] = value["protocol"]
    if "status_code" in value:
        out["statusCode"] = value["status_code"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "headers" in value:
        out["headers"] = value["headers"]
    if "body" in value:
        out["body"] = value["body"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionDataResponse:
    out: InspectionDataResponse = {}  # type: ignore[typeddict-item]
    if data.get("protocol") is not None:
        out["protocol"] = data["protocol"]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("headers") is not None:
        out["headers"] = data["headers"]
    if data.get("body") is not None:
        out["body"] = data["body"]
    return out
