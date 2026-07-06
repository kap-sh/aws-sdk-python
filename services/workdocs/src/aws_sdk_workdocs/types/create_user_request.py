"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workdocs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.authentication_header_type
    import aws_sdk_workdocs.types.email_address_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.password_type
    import aws_sdk_workdocs.types.storage_rule_type
    import aws_sdk_workdocs.types.time_zone_id_type
    import aws_sdk_workdocs.types.user_attribute_value_type
    import aws_sdk_workdocs.types.username_type


class CreateUserRequest(TypedDict, closed=True):
    organization_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the organization.</p>"""
    username: "aws_sdk_workdocs.types.username_type.UsernameType"
    """<p>The login name of the user.</p>"""
    email_address: NotRequired[
        "aws_sdk_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""
    given_name: (
        "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    )
    """<p>The given name of the user.</p>"""
    surname: "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    """<p>The surname of the user.</p>"""
    password: "aws_sdk_workdocs.types.password_type.PasswordType"
    """<p>The password of the user.</p>"""
    time_zone_id: NotRequired["aws_sdk_workdocs.types.time_zone_id_type.TimeZoneIdType"]
    """<p>The time zone ID of the user.</p>"""
    storage_rule: NotRequired[
        "aws_sdk_workdocs.types.storage_rule_type.StorageRuleType"
    ]
    """<p>The amount of storage for the user.</p>"""
    authentication_token: NotRequired[
        "aws_sdk_workdocs.types.authentication_header_type.AuthenticationHeaderType"
    ]
    """<p>Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserRequest) -> dict:
    out: dict = {}
    if "organization_id" in value:
        out["OrganizationId"] = value["organization_id"]
    out["Username"] = value["username"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    out["GivenName"] = value["given_name"]
    out["Surname"] = value["surname"]
    out["Password"] = value["password"]
    if "time_zone_id" in value:
        out["TimeZoneId"] = value["time_zone_id"]
    if "storage_rule" in value:
        import aws_sdk_workdocs.types.storage_rule_type

        out["StorageRule"] = aws_sdk_workdocs.types.storage_rule_type.serialize_json(
            value["storage_rule"]
        )
    return out


def deserialize_json(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("CreateUserRequest.username required")
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    else:
        raise DeserializationError("CreateUserRequest.given_name required")
    if "Surname" in data:
        out["surname"] = data["Surname"]
    else:
        raise DeserializationError("CreateUserRequest.surname required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("CreateUserRequest.password required")
    if "TimeZoneId" in data:
        out["time_zone_id"] = data["TimeZoneId"]
    if "StorageRule" in data:
        import aws_sdk_workdocs.types.storage_rule_type

        out["storage_rule"] = aws_sdk_workdocs.types.storage_rule_type.deserialize_json(
            data["StorageRule"]
        )
    return out
