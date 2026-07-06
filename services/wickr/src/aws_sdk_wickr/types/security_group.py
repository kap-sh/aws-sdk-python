"""Generated from Smithy shape ``com.amazonaws.wickr#SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.security_group_settings


class SecurityGroup(TypedDict, closed=True):
    active_members: "int"
    """<p>The number of active user members currently in the security group.</p>"""
    bot_members: "int"
    """<p>The number of bot members currently in the security group.</p>"""
    active_directory_guid: NotRequired[
        "aws_sdk_wickr.types.generic_string.GenericString"
    ]
    """<p>The GUID of the Active Directory group associated with this security group, if synchronized with LDAP.</p>"""
    id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The unique identifier of the security group.</p>"""
    is_default: "bool"
    """<p>Indicates whether this is the default security group for the network. Each network has only one default group.</p>"""
    name: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The human-readable name of the security group.</p>"""
    modified: "int"
    """<p>The timestamp when the security group was last modified, specified in epoch seconds.</p>"""
    security_group_settings: (
        "aws_sdk_wickr.types.security_group_settings.SecurityGroupSettings"
    )
    """<p>The comprehensive configuration settings that define capabilities and restrictions for members of this security group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroup) -> dict:
    out: dict = {}
    out["activeMembers"] = value["active_members"]
    out["botMembers"] = value["bot_members"]
    if "active_directory_guid" in value:
        out["activeDirectoryGuid"] = value["active_directory_guid"]
    out["id"] = value["id"]
    out["isDefault"] = value["is_default"]
    out["name"] = value["name"]
    out["modified"] = value["modified"]
    import aws_sdk_wickr.types.security_group_settings

    out["securityGroupSettings"] = (
        aws_sdk_wickr.types.security_group_settings.serialize_json(
            value["security_group_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> SecurityGroup:
    out: SecurityGroup = {}  # type: ignore[typeddict-item]
    if "activeMembers" in data:
        out["active_members"] = data["activeMembers"]
    else:
        raise DeserializationError("SecurityGroup.active_members required")
    if "botMembers" in data:
        out["bot_members"] = data["botMembers"]
    else:
        raise DeserializationError("SecurityGroup.bot_members required")
    if "activeDirectoryGuid" in data:
        out["active_directory_guid"] = data["activeDirectoryGuid"]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("SecurityGroup.id required")
    if "isDefault" in data:
        out["is_default"] = data["isDefault"]
    else:
        raise DeserializationError("SecurityGroup.is_default required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SecurityGroup.name required")
    if "modified" in data:
        out["modified"] = data["modified"]
    else:
        raise DeserializationError("SecurityGroup.modified required")
    if "securityGroupSettings" in data:
        import aws_sdk_wickr.types.security_group_settings

        out["security_group_settings"] = (
            aws_sdk_wickr.types.security_group_settings.deserialize_json(
                data["securityGroupSettings"]
            )
        )
    else:
        raise DeserializationError("SecurityGroup.security_group_settings required")
    return out
