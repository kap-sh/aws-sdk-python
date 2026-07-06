"""Generated from Smithy shape ``com.amazonaws.chime#User``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.alexa_for_business_metadata
    import aws_sdk_chime.types.email_address
    import aws_sdk_chime.types.invite_status
    import aws_sdk_chime.types.iso8601_timestamp
    import aws_sdk_chime.types.license
    import aws_sdk_chime.types.registration_status
    import aws_sdk_chime.types.sensitive_string
    import aws_sdk_chime.types.string
    import aws_sdk_chime.types.user_type


class User(TypedDict, closed=True):
    user_id: "aws_sdk_chime.types.string.String"
    """<p>The user ID.</p>"""
    account_id: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The Amazon Chime account ID.</p>"""
    primary_email: NotRequired["aws_sdk_chime.types.email_address.EmailAddress"]
    """<p>The primary email address of the user.</p>"""
    primary_provisioned_number: NotRequired[
        "aws_sdk_chime.types.sensitive_string.SensitiveString"
    ]
    """<p>The primary phone number associated with the user.</p>"""
    display_name: NotRequired["aws_sdk_chime.types.sensitive_string.SensitiveString"]
    """<p>The display name of the user.</p>"""
    license_type: NotRequired["aws_sdk_chime.types.license.License"]
    """<p>The license type for the user.</p>"""
    user_type: NotRequired["aws_sdk_chime.types.user_type.UserType"]
    """<p>The user type.</p>"""
    user_registration_status: NotRequired[
        "aws_sdk_chime.types.registration_status.RegistrationStatus"
    ]
    """<p>The user registration status.</p>"""
    user_invitation_status: NotRequired[
        "aws_sdk_chime.types.invite_status.InviteStatus"
    ]
    """<p>The user invite status.</p>"""
    registered_on: NotRequired["aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"]
    """<p>Date and time when the user is registered, in ISO 8601 format.</p>"""
    invited_on: NotRequired["aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"]
    """<p>Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.</p>"""
    alexa_for_business_metadata: NotRequired[
        "aws_sdk_chime.types.alexa_for_business_metadata.AlexaForBusinessMetadata"
    ]
    """<p>The Alexa for Business metadata.</p>"""
    personal_pin: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>The user's personal meeting PIN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: User) -> dict:
    out: dict = {}
    out["UserId"] = value["user_id"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "primary_email" in value:
        out["PrimaryEmail"] = value["primary_email"]
    if "primary_provisioned_number" in value:
        out["PrimaryProvisionedNumber"] = value["primary_provisioned_number"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "license_type" in value:
        import aws_sdk_chime.types.license

        out["LicenseType"] = aws_sdk_chime.types.license.serialize_json(
            value["license_type"]
        )
    if "user_type" in value:
        import aws_sdk_chime.types.user_type

        out["UserType"] = aws_sdk_chime.types.user_type.serialize_json(
            value["user_type"]
        )
    if "user_registration_status" in value:
        import aws_sdk_chime.types.registration_status

        out["UserRegistrationStatus"] = (
            aws_sdk_chime.types.registration_status.serialize_json(
                value["user_registration_status"]
            )
        )
    if "user_invitation_status" in value:
        import aws_sdk_chime.types.invite_status

        out["UserInvitationStatus"] = aws_sdk_chime.types.invite_status.serialize_json(
            value["user_invitation_status"]
        )
    if "registered_on" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["RegisteredOn"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["registered_on"]
        )
    if "invited_on" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["InvitedOn"] = aws_sdk_chime.types.iso8601_timestamp.serialize_json(
            value["invited_on"]
        )
    if "alexa_for_business_metadata" in value:
        import aws_sdk_chime.types.alexa_for_business_metadata

        out["AlexaForBusinessMetadata"] = (
            aws_sdk_chime.types.alexa_for_business_metadata.serialize_json(
                value["alexa_for_business_metadata"]
            )
        )
    if "personal_pin" in value:
        out["PersonalPIN"] = value["personal_pin"]
    return out


def deserialize_json(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("User.user_id required")
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "PrimaryEmail" in data:
        out["primary_email"] = data["PrimaryEmail"]
    if "PrimaryProvisionedNumber" in data:
        out["primary_provisioned_number"] = data["PrimaryProvisionedNumber"]
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "LicenseType" in data:
        import aws_sdk_chime.types.license

        out["license_type"] = aws_sdk_chime.types.license.deserialize_json(
            data["LicenseType"]
        )
    if "UserType" in data:
        import aws_sdk_chime.types.user_type

        out["user_type"] = aws_sdk_chime.types.user_type.deserialize_json(
            data["UserType"]
        )
    if "UserRegistrationStatus" in data:
        import aws_sdk_chime.types.registration_status

        out["user_registration_status"] = (
            aws_sdk_chime.types.registration_status.deserialize_json(
                data["UserRegistrationStatus"]
            )
        )
    if "UserInvitationStatus" in data:
        import aws_sdk_chime.types.invite_status

        out["user_invitation_status"] = (
            aws_sdk_chime.types.invite_status.deserialize_json(
                data["UserInvitationStatus"]
            )
        )
    if "RegisteredOn" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["registered_on"] = aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
            data["RegisteredOn"]
        )
    if "InvitedOn" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["invited_on"] = aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
            data["InvitedOn"]
        )
    if "AlexaForBusinessMetadata" in data:
        import aws_sdk_chime.types.alexa_for_business_metadata

        out["alexa_for_business_metadata"] = (
            aws_sdk_chime.types.alexa_for_business_metadata.deserialize_json(
                data["AlexaForBusinessMetadata"]
            )
        )
    if "PersonalPIN" in data:
        out["personal_pin"] = data["PersonalPIN"]
    return out
