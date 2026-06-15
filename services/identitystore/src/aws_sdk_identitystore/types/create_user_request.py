"""Generated from Smithy shape ``com.amazonaws.identitystore#CreateUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.addresses
    import aws_sdk_identitystore.types.emails
    import aws_sdk_identitystore.types.extensions
    import aws_sdk_identitystore.types.identity_store_id
    import aws_sdk_identitystore.types.name
    import aws_sdk_identitystore.types.phone_numbers
    import aws_sdk_identitystore.types.photos
    import aws_sdk_identitystore.types.roles
    import aws_sdk_identitystore.types.sensitive_string_type
    import aws_sdk_identitystore.types.user_name


class CreateUserRequest(TypedDict):
    identity_store_id: "aws_sdk_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_name: NotRequired["aws_sdk_identitystore.types.user_name.UserName"]
    """<p>A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store. <code>Administrator</code> and <code>AWSAdministrators</code> are reserved names and can't be used for users or groups.</p>"""
    name: NotRequired["aws_sdk_identitystore.types.name.Name"]
    """<p>An object containing the name of the user. When used in IAM Identity Center, this parameter is required.</p>"""
    display_name: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    r"""<p>A string containing the name of the user. This value is typically formatted for display when the user is referenced. For example, \"John Doe.\" When used in IAM Identity Center, this parameter is required.</p>"""
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
    r"""<p>A string containing the preferred language of the user. For example, \"American English\" or \"en-us.\"</p>"""
    locale: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the geographical region or location of the user.</p>"""
    timezone: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing the time zone of the user.</p>"""
    photos: NotRequired["aws_sdk_identitystore.types.photos.Photos"]
    """<p>A list of photos associated with the user. You can add up to 3 photos per user. Each photo can include a value, type, display name, and primary designation.</p>"""
    website: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's personal website or blog URL. This field allows users to provide a link to their personal or professional website.</p>"""
    birthdate: NotRequired[
        "aws_sdk_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>The user's birthdate in YYYY-MM-DD format. This field supports standard date format for storing personal information.</p>"""
    roles: NotRequired["aws_sdk_identitystore.types.roles.Roles"]
    """<p>A list of <code>Role</code> objects containing roles associated with the user.</p>"""
    extensions: NotRequired["aws_sdk_identitystore.types.extensions.Extensions"]
    """<p>A map with additional attribute extensions for the user. Each map key corresponds to an extension name, while map values represent extension data in <code>Document</code> type (not supported by Java V1, Go V1 and older versions of the CLI). <code>aws:identitystore:enterprise</code> is the only supported extension name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
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
    if "extensions" in value:
        import aws_sdk_identitystore.types.extensions

        out["Extensions"] = (
            aws_sdk_identitystore.types.extensions.serialize_aws_json_1_1(
                value["extensions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "IdentityStoreId" in data:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("CreateUserRequest.identity_store_id required")
    if "UserName" in data:
        out["user_name"] = data["UserName"]
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
    if "Extensions" in data:
        import aws_sdk_identitystore.types.extensions

        out["extensions"] = (
            aws_sdk_identitystore.types.extensions.deserialize_aws_json_1_1(
                data["Extensions"]
            )
        )
    return out
