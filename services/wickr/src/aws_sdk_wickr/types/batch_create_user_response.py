"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.batch_user_error_response_items
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.users


class BatchCreateUserResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch operation.</p>"""
    successful: NotRequired["aws_sdk_wickr.types.users.Users"]
    """<p>A list of user objects that were successfully created, including their assigned user IDs and invite codes.</p>"""
    failed: NotRequired[
        "aws_sdk_wickr.types.batch_user_error_response_items.BatchUserErrorResponseItems"
    ]
    """<p>A list of user creation attempts that failed, including error details explaining why each user could not be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import aws_sdk_wickr.types.users

        out["successful"] = aws_sdk_wickr.types.users.serialize_json(
            value["successful"]
        )
    if "failed" in value:
        import aws_sdk_wickr.types.batch_user_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_user_error_response_items.serialize_json(
                value["failed"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchCreateUserResponse:
    out: BatchCreateUserResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "successful" in data:
        import aws_sdk_wickr.types.users

        out["successful"] = aws_sdk_wickr.types.users.deserialize_json(
            data["successful"]
        )
    if "failed" in data:
        import aws_sdk_wickr.types.batch_user_error_response_items

        out["failed"] = (
            aws_sdk_wickr.types.batch_user_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out
