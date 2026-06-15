"""Generated from Smithy shape ``com.amazonaws.managedblockchain#MemberFabricConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.password_string
    import aws_sdk_managedblockchain.types.username_string


class MemberFabricConfiguration(TypedDict):
    admin_username: "aws_sdk_managedblockchain.types.username_string.UsernameString"
    """<p>The user name for the member's initial administrative user.</p>"""
    admin_password: "aws_sdk_managedblockchain.types.password_string.PasswordString"
    r"""<p>The password for the member's initial administrative user. The <code>AdminPassword</code> must be at least 8 characters long and no more than 32 characters. It must contain at least one uppercase letter, one lowercase letter, and one digit. It cannot have a single quotation mark (‘), a double quotation marks (“), a forward slash(/), a backward slash(\), @, or a space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemberFabricConfiguration) -> dict:
    out: dict = {}
    out["AdminUsername"] = value["admin_username"]
    out["AdminPassword"] = value["admin_password"]
    return out


def deserialize_json(data: dict) -> MemberFabricConfiguration:
    out: MemberFabricConfiguration = {}  # type: ignore[typeddict-item]
    if "AdminUsername" in data:
        out["admin_username"] = data["AdminUsername"]
    else:
        raise DeserializationError("MemberFabricConfiguration.admin_username required")
    if "AdminPassword" in data:
        out["admin_password"] = data["AdminPassword"]
    else:
        raise DeserializationError("MemberFabricConfiguration.admin_password required")
    return out
