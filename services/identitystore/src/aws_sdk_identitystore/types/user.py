"""Generated from Smithy shape ``com.amazonaws.identitystore#User``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.addresses
    import aws_sdk_identitystore.types.date_type
    import aws_sdk_identitystore.types.emails
    import aws_sdk_identitystore.types.extensions
    import aws_sdk_identitystore.types.external_ids
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.name
    import aws_sdk_identitystore.types.phone_numbers
    import aws_sdk_identitystore.types.photos
    import aws_sdk_identitystore.types.resource_id
    import aws_sdk_identitystore.types.roles
    import aws_sdk_identitystore.types.sensitive_string_type
    import aws_sdk_identitystore.types.string_type
    import aws_sdk_identitystore.types.user_name
    import aws_sdk_identitystore.types.user_status


class User(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "aws_sdk_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    user_name: NotRequired["aws_sdk_identitystore.types.user_name.UserName"]
    """<p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.</p>"""
    external_ids: NotRequired["aws_sdk_identitystore.types.external_ids.ExternalIds"]
    """<p>A list of <code>ExternalId</code> objects that contains the identifiers issued to this resource by an external identity provider.</p>"""
    name: NotRequired["aws_sdk_identitystore.types.name.Name"]
    """<p>An object containing the name of the user.</p>"""
    display_name: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the name of the user that is formatted for display when the user is referenced. For example, \"John Doe.\"</p> <p>Prefix search supports a maximum of 1,000 characters for the string.</p>"""
    nick_name: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing an alternate name for the user.</p>"""
    profile_url: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a URL that might be associated with the user.</p>"""
    emails: NotRequired["aws_sdk_identitystore.types.emails.Emails"]
    """<p>A list of <code>Email</code> objects containing email addresses associated with the user.</p>"""
    addresses: NotRequired["aws_sdk_identitystore.types.addresses.Addresses"]
    """<p>A list of <code>Address</code> objects containing addresses associated with the user.</p>"""
    phone_numbers: NotRequired["aws_sdk_identitystore.types.phone_numbers.PhoneNumbers"]
    """<p>A list of <code>PhoneNumber</code> objects containing phone numbers associated with the user.</p>"""
    user_type: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.</p>"""
    title: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.</p>"""
    preferred_language: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the preferred language of the user. For example, \"American English\" or \"en-us.\"</p>"""
    locale: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the geographical region or location of the user.</p>"""
    timezone: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the time zone of the user.</p>"""
    user_status: NotRequired["aws_sdk_identitystore.types.user_status.UserStatus"]
    """<p>The current status of the user account.</p>"""
    photos: NotRequired["aws_sdk_identitystore.types.photos.Photos"]
    """<p>A list of photos associated with the user. Users can have up to 3 photos with metadata including type, display name, and primary designation.</p>"""
    website: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's personal website or blog URL. This field stores website information for personal or professional use.</p>"""
    birthdate: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's birthdate in YYYY-MM-DD format. This field stores personal birthdate information for the user.</p>"""
    roles: NotRequired["aws_sdk_identitystore.types.roles.Roles"]
    """<p>A list of <code>Role</code> objects containing roles associated with the user.</p>"""
    created_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the user was created.</p>"""
    created_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the user.</p>"""
    updated_at: NotRequired["aws_sdk_identitystore.types.date_type.DateType"]
    """<p>The date and time the user was last updated.</p>"""
    updated_by: NotRequired["aws_sdk_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the user.</p>"""
    extensions: NotRequired["aws_sdk_identitystore.types.extensions.Extensions"]
    """<p>A map of explicitly requested attribute extensions associated with the user. Not populated if the user has no requested extensions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: User) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "external_ids" in value:
        import aws_sdk_identitystore.types.external_ids

        out["ExternalIds"] = (
            aws_sdk_identitystore.types.external_ids.serialize_aws_json_1_1(
                value["external_ids"]
            )
        )
    if "name" in value:
        import aws_sdk_identitystore.types.name

        out["Name"] = aws_sdk_identitystore.types.name.serialize_aws_json_1_1(
            value["name"]
        )
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "nick_name" in value:
        out["NickName"] = value["nick_name"]
    if "profile_url" in value:
        out["ProfileUrl"] = value["profile_url"]
    if "emails" in value:
        import aws_sdk_identitystore.types.emails

        out["Emails"] = aws_sdk_identitystore.types.emails.serialize_aws_json_1_1(
            value["emails"]
        )
    if "addresses" in value:
        import aws_sdk_identitystore.types.addresses

        out["Addresses"] = aws_sdk_identitystore.types.addresses.serialize_aws_json_1_1(
            value["addresses"]
        )
    if "phone_numbers" in value:
        import aws_sdk_identitystore.types.phone_numbers

        out["PhoneNumbers"] = (
            aws_sdk_identitystore.types.phone_numbers.serialize_aws_json_1_1(
                value["phone_numbers"]
            )
        )
    if "user_type" in value:
        out["UserType"] = value["user_type"]
    if "title" in value:
        out["Title"] = value["title"]
    if "preferred_language" in value:
        out["PreferredLanguage"] = value["preferred_language"]
    if "locale" in value:
        out["Locale"] = value["locale"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "user_status" in value:
        import aws_sdk_identitystore.types.user_status

        out["UserStatus"] = (
            aws_sdk_identitystore.types.user_status.serialize_aws_json_1_1(
                value["user_status"]
            )
        )
    if "photos" in value:
        import aws_sdk_identitystore.types.photos

        out["Photos"] = aws_sdk_identitystore.types.photos.serialize_aws_json_1_1(
            value["photos"]
        )
    if "website" in value:
        out["Website"] = value["website"]
    if "birthdate" in value:
        out["Birthdate"] = value["birthdate"]
    if "roles" in value:
        import aws_sdk_identitystore.types.roles

        out["Roles"] = aws_sdk_identitystore.types.roles.serialize_aws_json_1_1(
            value["roles"]
        )
    if "created_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["CreatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_at" in value:
        import aws_sdk_identitystore.types.date_type

        out["UpdatedAt"] = aws_sdk_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    if "extensions" in value:
        import aws_sdk_identitystore.types.extensions

        out["Extensions"] = (
            aws_sdk_identitystore.types.extensions.serialize_aws_json_1_1(
                value["extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> User:
    out: User = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("User.identity_store_id required")
    if "UserId" in data:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("User.user_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
    if "ExternalIds" in data:
        import aws_sdk_identitystore.types.external_ids

        out["external_ids"] = (
            aws_sdk_identitystore.types.external_ids.deserialize_aws_json_1_1(
                data["ExternalIds"]
            )
        )
    if "Name" in data:
        import aws_sdk_identitystore.types.name

        out["name"] = aws_sdk_identitystore.types.name.deserialize_aws_json_1_1(
            data["Name"]
        )
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "NickName" in data:
        out["nick_name"] = data["NickName"]
    if "ProfileUrl" in data:
        out["profile_url"] = data["ProfileUrl"]
    if "Emails" in data:
        import aws_sdk_identitystore.types.emails

        out["emails"] = aws_sdk_identitystore.types.emails.deserialize_aws_json_1_1(
            data["Emails"]
        )
    if "Addresses" in data:
        import aws_sdk_identitystore.types.addresses

        out["addresses"] = (
            aws_sdk_identitystore.types.addresses.deserialize_aws_json_1_1(
                data["Addresses"]
            )
        )
    if "PhoneNumbers" in data:
        import aws_sdk_identitystore.types.phone_numbers

        out["phone_numbers"] = (
            aws_sdk_identitystore.types.phone_numbers.deserialize_aws_json_1_1(
                data["PhoneNumbers"]
            )
        )
    if "UserType" in data:
        out["user_type"] = data["UserType"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "PreferredLanguage" in data:
        out["preferred_language"] = data["PreferredLanguage"]
    if "Locale" in data:
        out["locale"] = data["Locale"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "UserStatus" in data:
        import aws_sdk_identitystore.types.user_status

        out["user_status"] = (
            aws_sdk_identitystore.types.user_status.deserialize_aws_json_1_1(
                data["UserStatus"]
            )
        )
    if "Photos" in data:
        import aws_sdk_identitystore.types.photos

        out["photos"] = aws_sdk_identitystore.types.photos.deserialize_aws_json_1_1(
            data["Photos"]
        )
    if "Website" in data:
        out["website"] = data["Website"]
    if "Birthdate" in data:
        out["birthdate"] = data["Birthdate"]
    if "Roles" in data:
        import aws_sdk_identitystore.types.roles

        out["roles"] = aws_sdk_identitystore.types.roles.deserialize_aws_json_1_1(
            data["Roles"]
        )
    if "CreatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["created_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "UpdatedAt" in data:
        import aws_sdk_identitystore.types.date_type

        out["updated_at"] = (
            aws_sdk_identitystore.types.date_type.deserialize_aws_json_1_1(
                data["UpdatedAt"]
            )
        )
    if "UpdatedBy" in data:
        out["updated_by"] = data["UpdatedBy"]
    if "Extensions" in data:
        import aws_sdk_identitystore.types.extensions

        out["extensions"] = (
            aws_sdk_identitystore.types.extensions.deserialize_aws_json_1_1(
                data["Extensions"]
            )
        )
    return out
