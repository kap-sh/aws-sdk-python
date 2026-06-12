"""Generated from Smithy shape ``com.amazonaws.wickr#CreateSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.security_group_settings_request


class CreateSecurityGroupRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the security group will be created.</p>"""
    name: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The name for the new security group.</p>"""
    security_group_settings: "aws_sdk_wickr.types.security_group_settings_request.SecurityGroupSettingsRequest"
    """<p>The configuration settings for the security group, including permissions, federation settings, and feature controls.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_wickr.types.security_group_settings_request

    out["securityGroupSettings"] = (
        aws_sdk_wickr.types.security_group_settings_request.serialize_json(
            value["security_group_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSecurityGroupRequest:
    out: CreateSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateSecurityGroupRequest.name required")
    if "securityGroupSettings" in data:
        import aws_sdk_wickr.types.security_group_settings_request

        out["security_group_settings"] = (
            aws_sdk_wickr.types.security_group_settings_request.deserialize_json(
                data["securityGroupSettings"]
            )
        )
    else:
        raise DeserializationError(
            "CreateSecurityGroupRequest.security_group_settings required"
        )
    return out
