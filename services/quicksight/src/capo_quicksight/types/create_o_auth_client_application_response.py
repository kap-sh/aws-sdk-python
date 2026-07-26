"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateOAuthClientApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.o_auth_client_application_id
    import capo_quicksight.types.resource_status
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class CreateOAuthClientApplicationResponse(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the OAuthClientApplication.</p>"""
    o_auth_client_application_id: NotRequired[
        "capo_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    ]
    """<p>The ID of the OAuthClientApplication. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    creation_status: NotRequired["capo_quicksight.types.resource_status.ResourceStatus"]
    """<p>The status of creating the OAuthClientApplication.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOAuthClientApplicationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "o_auth_client_application_id" in value:
        out["OAuthClientApplicationId"] = value["o_auth_client_application_id"]
    if "creation_status" in value:
        import capo_quicksight.types.resource_status

        out["CreationStatus"] = capo_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateOAuthClientApplicationResponse:
    out: CreateOAuthClientApplicationResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "OAuthClientApplicationId" in data:
        out["o_auth_client_application_id"] = data["OAuthClientApplicationId"]
    if "CreationStatus" in data:
        import capo_quicksight.types.resource_status

        out["creation_status"] = capo_quicksight.types.resource_status.deserialize_json(
            data["CreationStatus"]
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
