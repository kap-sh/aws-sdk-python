"""Generated from Smithy shape ``com.amazonaws.datazone#GetUserProfileInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.user_identifier
    import aws_sdk_datazone.types.user_profile_type


class GetUserProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>the ID of the Amazon DataZone domain the data portal of which you want to get.</p>"""
    user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier"
    """<p>The identifier of the user for which you want to get the user profile.</p>"""
    type: NotRequired["aws_sdk_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserProfileInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserProfileInput:
    out: GetUserProfileInput = {}  # type: ignore[typeddict-item]
    return out
