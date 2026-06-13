"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteOAuthClientApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.o_auth_client_application_id


class DeleteOAuthClientApplicationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    o_auth_client_application_id: (
        "aws_sdk_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    )
    """<p>The ID of the OAuthClientApplication that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOAuthClientApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOAuthClientApplicationRequest:
    out: DeleteOAuthClientApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
