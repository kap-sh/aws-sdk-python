"""Generated from Smithy shape ``com.amazonaws.chime#BatchUnsuspendUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.user_id_list


class BatchUnsuspendUserRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_id_list: "aws_sdk_chime.types.user_id_list.UserIdList"
    """<p>The request containing the user IDs to unsuspend.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUnsuspendUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.user_id_list

    out["UserIdList"] = aws_sdk_chime.types.user_id_list.serialize_json(
        value["user_id_list"]
    )
    return out


def deserialize_json(data: dict) -> BatchUnsuspendUserRequest:
    out: BatchUnsuspendUserRequest = {}  # type: ignore[typeddict-item]
    if "UserIdList" in data:
        import aws_sdk_chime.types.user_id_list

        out["user_id_list"] = aws_sdk_chime.types.user_id_list.deserialize_json(
            data["UserIdList"]
        )
    else:
        raise DeserializationError("BatchUnsuspendUserRequest.user_id_list required")
    return out
