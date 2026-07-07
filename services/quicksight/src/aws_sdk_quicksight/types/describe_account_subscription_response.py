"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAccountSubscriptionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.account_info
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeAccountSubscriptionResponse(TypedDict, closed=True):
    account_info: NotRequired["aws_sdk_quicksight.types.account_info.AccountInfo"]
    """<p>A structure that contains the following elements:</p> <ul> <li> <p>Your Quick Sight account name.</p> </li> <li> <p>The edition of Quick Sight that your account is using.</p> </li> <li> <p>The notification email address that is associated with the Amazon Quick Sight account. </p> </li> <li> <p>The authentication type of the Quick Sight account.</p> </li> <li> <p>The status of the Quick Sight account's subscription.</p> </li> </ul>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountSubscriptionResponse) -> dict:
    out: dict = {}
    if "account_info" in value:
        import aws_sdk_quicksight.types.account_info

        out["AccountInfo"] = aws_sdk_quicksight.types.account_info.serialize_json(
            value["account_info"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAccountSubscriptionResponse:
    out: DescribeAccountSubscriptionResponse = {}  # type: ignore[typeddict-item]
    if "AccountInfo" in data:
        import aws_sdk_quicksight.types.account_info

        out["account_info"] = aws_sdk_quicksight.types.account_info.deserialize_json(
            data["AccountInfo"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
