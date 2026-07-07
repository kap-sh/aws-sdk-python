"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.user


class DescribeUserResponse(TypedDict, closed=True):
    user: NotRequired["aws_sdk_quicksight.types.user.User"]
    """<p>The user name.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserResponse) -> dict:
    out: dict = {}
    if "user" in value:
        import aws_sdk_quicksight.types.user

        out["User"] = aws_sdk_quicksight.types.user.serialize_json(value["user"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeUserResponse:
    out: DescribeUserResponse = {}  # type: ignore[typeddict-item]
    if "User" in data:
        import aws_sdk_quicksight.types.user

        out["user"] = aws_sdk_quicksight.types.user.deserialize_json(data["User"])
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
