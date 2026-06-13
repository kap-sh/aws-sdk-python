"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateUserProfileInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.user_identifier
    import aws_sdk_datazone.types.user_profile_status
    import aws_sdk_datazone.types.user_profile_type


class UpdateUserProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a user profile is updated.</p>"""
    user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier"
    """<p>The identifier of the user whose user profile is to be updated.</p>"""
    type: NotRequired["aws_sdk_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile that are to be updated.</p>"""
    status: "aws_sdk_datazone.types.user_profile_status.UserProfileStatus"
    """<p>The status of the user profile that are to be updated.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserProfileInput) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_datazone.types.user_profile_type

        out["type"] = aws_sdk_datazone.types.user_profile_type.serialize_json(
            value["type"]
        )
    import aws_sdk_datazone.types.user_profile_status

    out["status"] = aws_sdk_datazone.types.user_profile_status.serialize_json(
        value["status"]
    )
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    return out


def deserialize_json(data: dict) -> UpdateUserProfileInput:
    out: UpdateUserProfileInput = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_datazone.types.user_profile_type

        out["type"] = aws_sdk_datazone.types.user_profile_type.deserialize_json(
            data["type"]
        )
    if "status" in data:
        import aws_sdk_datazone.types.user_profile_status

        out["status"] = aws_sdk_datazone.types.user_profile_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateUserProfileInput.status required")
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    return out
