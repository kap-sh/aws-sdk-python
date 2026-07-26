"""Generated from Smithy shape ``com.amazonaws.wickr#BatchToggleUserSuspendStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.batch_user_error_response_items
    import capo_wickr.types.batch_user_success_response_items
    import capo_wickr.types.generic_string


class BatchToggleUserSuspendStatusResponse(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch suspend status toggle operation.</p>"""
    successful: NotRequired[
        "capo_wickr.types.batch_user_success_response_items.BatchUserSuccessResponseItems"
    ]
    """<p>A list of user IDs whose suspend status was successfully toggled.</p>"""
    failed: NotRequired[
        "capo_wickr.types.batch_user_error_response_items.BatchUserErrorResponseItems"
    ]
    """<p>A list of suspend status toggle attempts that failed, including error details explaining why each user's status could not be changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchToggleUserSuspendStatusResponse) -> dict:
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


def deserialize_json(data: dict) -> BatchToggleUserSuspendStatusResponse:
    out: BatchToggleUserSuspendStatusResponse = {}  # type: ignore[typeddict-item]
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
