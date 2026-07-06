"""Generated from Smithy shape ``com.amazonaws.transfer#TestIdentityProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.message
    import aws_sdk_transfer.types.response
    import aws_sdk_transfer.types.status_code
    import aws_sdk_transfer.types.url


class TestIdentityProviderResponse(TypedDict, closed=True):
    response: NotRequired["aws_sdk_transfer.types.response.Response"]
    """<p>The response that is returned from your API Gateway or your Lambda function.</p>"""
    status_code: "aws_sdk_transfer.types.status_code.StatusCode"
    """<p>The HTTP status code that is the response from your API Gateway or your Lambda function.</p>"""
    message: NotRequired["aws_sdk_transfer.types.message.Message"]
    """<p>A message that indicates whether the test was successful or not.</p> <note> <p>If an empty string is returned, the most likely cause is that the authentication failed due to an incorrect username or password.</p> </note>"""
    url: "aws_sdk_transfer.types.url.Url"
    """<p>The endpoint of the service used to authenticate a user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TestIdentityProviderResponse) -> dict:
    out: dict = {}
    if "response" in value:
        out["Response"] = value["response"]
    out["StatusCode"] = value.get("status_code", 0)
    if "message" in value:
        out["Message"] = value["message"]
    out["Url"] = value["url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TestIdentityProviderResponse:
    out: TestIdentityProviderResponse = {}  # type: ignore[typeddict-item]
    if "Response" in data:
        out["response"] = data["Response"]
    if "StatusCode" in data:
        out["status_code"] = data["StatusCode"]
    else:
        out["status_code"] = 0
    if "Message" in data:
        out["message"] = data["Message"]
    if "Url" in data:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("TestIdentityProviderResponse.url required")
    return out
