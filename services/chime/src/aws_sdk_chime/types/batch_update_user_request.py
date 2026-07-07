"""Generated from Smithy shape ``com.amazonaws.chime#BatchUpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.update_user_request_item_list


class BatchUpdateUserRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    update_user_request_items: (
        "aws_sdk_chime.types.update_user_request_item_list.UpdateUserRequestItemList"
    )
    """<p>The request containing the user IDs and details to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.update_user_request_item_list

    out["UpdateUserRequestItems"] = (
        aws_sdk_chime.types.update_user_request_item_list.serialize_json(
            value["update_user_request_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateUserRequest:
    out: BatchUpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "UpdateUserRequestItems" in data:
        import aws_sdk_chime.types.update_user_request_item_list

        out["update_user_request_items"] = (
            aws_sdk_chime.types.update_user_request_item_list.deserialize_json(
                data["UpdateUserRequestItems"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateUserRequest.update_user_request_items required"
        )
    return out
