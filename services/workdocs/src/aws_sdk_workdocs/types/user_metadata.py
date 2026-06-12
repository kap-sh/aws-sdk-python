"""Generated from Smithy shape ``com.amazonaws.workdocs#UserMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.email_address_type
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.user_attribute_value_type
    import aws_sdk_workdocs.types.username_type


class UserMetadata(TypedDict):
    id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the user.</p>"""
    username: NotRequired["aws_sdk_workdocs.types.username_type.UsernameType"]
    """<p>The name of the user.</p>"""
    given_name: NotRequired[
        "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The given name of the user before a rename operation.</p>"""
    surname: NotRequired[
        "aws_sdk_workdocs.types.user_attribute_value_type.UserAttributeValueType"
    ]
    """<p>The surname of the user.</p>"""
    email_address: NotRequired[
        "aws_sdk_workdocs.types.email_address_type.EmailAddressType"
    ]
    """<p>The email address of the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "username" in value:
        out["Username"] = value["username"]
    if "given_name" in value:
        out["GivenName"] = value["given_name"]
    if "surname" in value:
        out["Surname"] = value["surname"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    return out


def deserialize_json(data: dict) -> UserMetadata:
    out: UserMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Username" in data:
        out["username"] = data["Username"]
    if "GivenName" in data:
        out["given_name"] = data["GivenName"]
    if "Surname" in data:
        out["surname"] = data["Surname"]
    if "EmailAddress" in data:
        out["email_address"] = data["EmailAddress"]
    return out
