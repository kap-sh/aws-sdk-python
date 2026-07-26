"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateIpRestrictionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class UpdateIpRestrictionResponse(TypedDict, closed=True):
    aws_account_id: NotRequired["capo_quicksight.types.aws_account_id.AwsAccountId"]
    """<p>The ID of the Amazon Web Services account that contains the IP rules.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIpRestrictionResponse) -> dict:
    out: dict = {}
    if "aws_account_id" in value:
        out["AwsAccountId"] = value["aws_account_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateIpRestrictionResponse:
    out: UpdateIpRestrictionResponse = {}  # type: ignore[typeddict-item]
    if "AwsAccountId" in data:
        out["aws_account_id"] = data["AwsAccountId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
