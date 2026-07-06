"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.update_user_details
    import aws_sdk_wickr.types.user_id


class UpdateUserRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the user to update.</p>"""
    user_id: "aws_sdk_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user to update.</p>"""
    user_details: NotRequired[
        "aws_sdk_wickr.types.update_user_details.UpdateUserDetails"
    ]
    """<p>An object containing the user details to be updated, such as name, password, security groups, and invite code settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "user_details" in value:
        import aws_sdk_wickr.types.update_user_details

        out["userDetails"] = aws_sdk_wickr.types.update_user_details.serialize_json(
            value["user_details"]
        )
    return out


def deserialize_json(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if "userId" in data:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("UpdateUserRequest.user_id required")
    if "userDetails" in data:
        import aws_sdk_wickr.types.update_user_details

        out["user_details"] = aws_sdk_wickr.types.update_user_details.deserialize_json(
            data["userDetails"]
        )
    return out
