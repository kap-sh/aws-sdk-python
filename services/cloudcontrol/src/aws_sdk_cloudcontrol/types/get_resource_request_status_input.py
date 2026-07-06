"""Generated from Smithy shape ``com.amazonaws.cloudcontrol#GetResourceRequestStatusInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cloudcontrol.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudcontrol.types.request_token


class GetResourceRequestStatusInput(TypedDict, closed=True):
    request_token: "aws_sdk_cloudcontrol.types.request_token.RequestToken"
    """<p>A unique token used to track the progress of the resource operation request.</p> <p>Request tokens are included in the <code>ProgressEvent</code> type returned by a resource operation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceRequestStatusInput) -> dict:
    out: dict = {}
    out["RequestToken"] = value["request_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceRequestStatusInput:
    out: GetResourceRequestStatusInput = {}  # type: ignore[typeddict-item]
    if "RequestToken" in data:
        out["request_token"] = data["RequestToken"]
    else:
        raise DeserializationError(
            "GetResourceRequestStatusInput.request_token required"
        )
    return out
