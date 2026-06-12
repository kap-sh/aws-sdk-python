"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.http_body
    import aws_sdk_sfn.types.http_headers
    import aws_sdk_sfn.types.http_protocol
    import aws_sdk_sfn.types.http_status_code
    import aws_sdk_sfn.types.http_status_message


class InspectionDataResponse(TypedDict):
    protocol: NotRequired["aws_sdk_sfn.types.http_protocol.HTTPProtocol"]
    """<p>The protocol used to return the HTTP response.</p>"""
    status_code: NotRequired["aws_sdk_sfn.types.http_status_code.HTTPStatusCode"]
    """<p>The HTTP response status code for the HTTP response.</p>"""
    status_message: NotRequired[
        "aws_sdk_sfn.types.http_status_message.HTTPStatusMessage"
    ]
    """<p>The message associated with the HTTP status code.</p>"""
    headers: NotRequired["aws_sdk_sfn.types.http_headers.HTTPHeaders"]
    """<p>The response headers associated with the HTTP response.</p>"""
    body: NotRequired["aws_sdk_sfn.types.http_body.HTTPBody"]
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
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    if "statusCode" in data:
        out["status_code"] = data["statusCode"]
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "headers" in data:
        out["headers"] = data["headers"]
    if "body" in data:
        out["body"] = data["body"]
    return out
