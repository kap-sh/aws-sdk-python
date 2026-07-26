"""Generated from Smithy shape ``com.amazonaws.quicksight#DeleteOAuthClientApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.o_auth_client_application_id


class DeleteOAuthClientApplicationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    o_auth_client_application_id: (
        "capo_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    )
    """<p>The ID of the OAuthClientApplication that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOAuthClientApplicationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOAuthClientApplicationRequest:
    out: DeleteOAuthClientApplicationRequest = {}  # type: ignore[typeddict-item]
    return out
