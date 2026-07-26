"""Generated from Smithy shape ``com.amazonaws.wickr#BatchReinviteUserResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.batch_user_error_response_items
    import capo_wickr.types.batch_user_success_response_items
    import capo_wickr.types.generic_string


class BatchReinviteUserResponse(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch reinvitation operation.</p>"""
    successful: NotRequired[
        "capo_wickr.types.batch_user_success_response_items.BatchUserSuccessResponseItems"
    ]
    """<p>A list of user IDs that were successfully reinvited.</p>"""
    failed: NotRequired[
        "capo_wickr.types.batch_user_error_response_items.BatchUserErrorResponseItems"
    ]
    """<p>A list of reinvitation attempts that failed, including error details explaining why each user could not be reinvited.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchReinviteUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import capo_wickr.types.batch_user_success_response_items

        out["successful"] = (
            capo_wickr.types.batch_user_success_response_items.serialize_json(
                value["successful"]
            )
        )
    if "failed" in value:
        import capo_wickr.types.batch_user_error_response_items

        out["failed"] = capo_wickr.types.batch_user_error_response_items.serialize_json(
            value["failed"]
        )
    return out


def deserialize_json(data: dict) -> BatchReinviteUserResponse:
    out: BatchReinviteUserResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "successful" in data:
        import capo_wickr.types.batch_user_success_response_items

        out["successful"] = (
            capo_wickr.types.batch_user_success_response_items.deserialize_json(
                data["successful"]
            )
        )
    if "failed" in data:
        import capo_wickr.types.batch_user_error_response_items

        out["failed"] = (
            capo_wickr.types.batch_user_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out
