"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateSecurityGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.security_group_settings


class UpdateSecurityGroupRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the security group to update.</p>"""
    group_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The unique identifier of the security group to update.</p>"""
    name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The new name for the security group.</p>"""
    security_group_settings: NotRequired[
        "capo_wickr.types.security_group_settings.SecurityGroupSettings"
    ]
    """<p>The updated configuration settings for the security group.</p> <p>Federation mode - 0 (Local federation), 1 (Restricted federation), 2 (Global federation) </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityGroupRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "security_group_settings" in value:
        import capo_wickr.types.security_group_settings

        out["securityGroupSettings"] = (
            capo_wickr.types.security_group_settings.serialize_json(
                value["security_group_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSecurityGroupRequest:
    out: UpdateSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "securityGroupSettings" in data:
        import capo_wickr.types.security_group_settings

        out["security_group_settings"] = (
            capo_wickr.types.security_group_settings.deserialize_json(
                data["securityGroupSettings"]
            )
        )
    return out
