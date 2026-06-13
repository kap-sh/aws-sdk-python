"""Generated from Smithy shape ``com.amazonaws.datazone#CreateUserProfileInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.user_identifier
    import aws_sdk_datazone.types.user_type


class CreateUserProfileInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which a user profile is created.</p>"""
    user_identifier: "aws_sdk_datazone.types.user_identifier.UserIdentifier"
    """<p>The identifier of the user for which the user profile is created.</p>"""
    user_type: NotRequired["aws_sdk_datazone.types.user_type.UserType"]
    """<p>The user type of the user for which the user profile is created.</p>"""
    session_name: NotRequired["str"]
    """<p>The session name for IAM role sessions.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserProfileInput) -> dict:
    out: dict = {}
    out["userIdentifier"] = value["user_identifier"]
    if "user_type" in value:
        import aws_sdk_datazone.types.user_type

        out["userType"] = aws_sdk_datazone.types.user_type.serialize_json(
            value["user_type"]
        )
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateUserProfileInput:
    out: CreateUserProfileInput = {}  # type: ignore[typeddict-item]
    if "userIdentifier" in data:
        out["user_identifier"] = data["userIdentifier"]
    else:
        raise DeserializationError("CreateUserProfileInput.user_identifier required")
    if "userType" in data:
        import aws_sdk_datazone.types.user_type

        out["user_type"] = aws_sdk_datazone.types.user_type.deserialize_json(
            data["userType"]
        )
    if "sessionName" in data:
        out["session_name"] = data["sessionName"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
