"""Generated from Smithy shape ``com.amazonaws.datazone#CreateUserProfileOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.user_profile_details
    import aws_sdk_datazone.types.user_profile_id
    import aws_sdk_datazone.types.user_profile_status
    import aws_sdk_datazone.types.user_profile_type


class CreateUserProfileOutput(TypedDict):
    domain_id: NotRequired["aws_sdk_datazone.types.domain_id.DomainId"]
    """<p>The identifier of the Amazon DataZone domain in which a user profile is created.</p>"""
    id: NotRequired["aws_sdk_datazone.types.user_profile_id.UserProfileId"]
    """<p>The identifier of the user profile.</p>"""
    type: NotRequired["aws_sdk_datazone.types.user_profile_type.UserProfileType"]
    """<p>The type of the user profile.</p>"""
    status: NotRequired["aws_sdk_datazone.types.user_profile_status.UserProfileStatus"]
    """<p>The status of the user profile.</p>"""
    details: NotRequired[
        "aws_sdk_datazone.types.user_profile_details.UserProfileDetails"
    ]
    """<p>The user profile details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserProfileOutput) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["domainId"] = value["domain_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import aws_sdk_datazone.types.user_profile_type

        out["type"] = aws_sdk_datazone.types.user_profile_type.serialize_json(
            value["type"]
        )
    if "status" in value:
        import aws_sdk_datazone.types.user_profile_status

        out["status"] = aws_sdk_datazone.types.user_profile_status.serialize_json(
            value["status"]
        )
    if "details" in value:
        import aws_sdk_datazone.types.user_profile_details

        out["details"] = aws_sdk_datazone.types.user_profile_details.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> CreateUserProfileOutput:
    out: CreateUserProfileOutput = {}  # type: ignore[typeddict-item]
    if "domainId" in data:
        out["domain_id"] = data["domainId"]
    if "id" in data:
        out["id"] = data["id"]
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
    if "details" in data:
        import aws_sdk_datazone.types.user_profile_details

        out["details"] = aws_sdk_datazone.types.user_profile_details.deserialize_json(
            data["details"]
        )
    return out
