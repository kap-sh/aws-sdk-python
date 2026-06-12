"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeleteUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_user_error_response_items
    import aws_sdk_wickr.types.batch_user_success_response_items
    import aws_sdk_wickr.types.generic_string


class BatchDeleteUserResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch deletion operation.</p>"""
    successful: NotRequired[
        "aws_sdk_wickr.types.batch_user_success_response_items.BatchUserSuccessResponseItems"
    ]
    """<p>A list of user IDs that were successfully deleted from the network.</p>"""
    failed: NotRequired[
        "aws_sdk_wickr.types.batch_user_error_response_items.BatchUserErrorResponseItems"
    ]
    """<p>A list of user deletion attempts that failed, including error details explaining why each user could not be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import aws_sdk_wickr.types.batch_user_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_user_success_response_items.serialize_json(
                value["successful"]
            )
        )
    if "failed" in value:
        import aws_sdk_wickr.types.batch_user_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_user_error_response_items.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteUserResponse:
    out: BatchDeleteUserResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "successful" in data:
        import aws_sdk_wickr.types.batch_user_success_response_items

        out["successful"] = (
            aws_sdk_wickr.types.batch_user_success_response_items.deserialize_json(
                data["successful"]
            )
        )
    if "failed" in data:
        import aws_sdk_wickr.types.batch_user_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_user_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out
