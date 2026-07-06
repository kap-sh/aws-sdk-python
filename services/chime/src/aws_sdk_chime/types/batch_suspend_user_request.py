"""Generated from Smithy shape ``com.amazonaws.chime#BatchSuspendUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string
    import aws_sdk_chime.types.user_id_list


class BatchSuspendUserRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_id_list: "aws_sdk_chime.types.user_id_list.UserIdList"
    """<p>The request containing the user IDs to suspend.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchSuspendUserRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime.types.user_id_list

    out["UserIdList"] = aws_sdk_chime.types.user_id_list.serialize_json(
        value["user_id_list"]
    )
    return out


def deserialize_json(data: dict) -> BatchSuspendUserRequest:
    out: BatchSuspendUserRequest = {}  # type: ignore[typeddict-item]
    if "UserIdList" in data:
        import aws_sdk_chime.types.user_id_list

        out["user_id_list"] = aws_sdk_chime.types.user_id_list.deserialize_json(
            data["UserIdList"]
        )
    else:
        raise DeserializationError("BatchSuspendUserRequest.user_id_list required")
    return out
