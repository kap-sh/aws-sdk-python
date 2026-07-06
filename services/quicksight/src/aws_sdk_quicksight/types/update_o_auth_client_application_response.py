"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateOAuthClientApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.o_auth_client_application_id
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateOAuthClientApplicationResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the OAuthClientApplication.</p>"""
    o_auth_client_application_id: NotRequired[
        "aws_sdk_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    ]
    """<p>The ID of the OAuthClientApplication. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    update_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The status of updating the OAuthClientApplication.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOAuthClientApplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "o_auth_client_application_id" in value:
        out["OAuthClientApplicationId"] = value["o_auth_client_application_id"]
    if "update_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["UpdateStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["update_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateOAuthClientApplicationResponse:
    out: UpdateOAuthClientApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OAuthClientApplicationId" in data:
        out["o_auth_client_application_id"] = data["OAuthClientApplicationId"]
    if "UpdateStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["update_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
