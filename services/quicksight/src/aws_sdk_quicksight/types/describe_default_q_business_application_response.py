"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDefaultQBusinessApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDefaultQBusinessApplicationResponse(TypedDict, closed=True):
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    application_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The ID of the Amazon Q Business application that is linked to the Quick Sight account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDefaultQBusinessApplicationResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    return out


def deserialize_json(data: dict) -> DescribeDefaultQBusinessApplicationResponse:
    out: DescribeDefaultQBusinessApplicationResponse = {}  # type: ignore[typeddict-item]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    return out
