"""Generated from Smithy shape ``com.amazonaws.transfer#DescribeWebAppRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.web_app_id


class DescribeWebAppRequest(TypedDict):
    web_app_id: "aws_sdk_transfer.types.web_app_id.WebAppId"
    """<p>Provide the unique identifier for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWebAppRequest) -> dict:
    out: dict = {}
    out["WebAppId"] = value["web_app_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWebAppRequest:
    out: DescribeWebAppRequest = {}  # type: ignore[typeddict-item]
    if "WebAppId" in data:
        out["web_app_id"] = data["WebAppId"]
    else:
        raise DeserializationError("DescribeWebAppRequest.web_app_id required")
    return out
