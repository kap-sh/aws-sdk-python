"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateOpenIdConnectGroupConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_verifiedpermissions.types.claim
    import aws_sdk_verifiedpermissions.types.group_entity_type


class UpdateOpenIdConnectGroupConfiguration(TypedDict, closed=True):
    group_claim: "aws_sdk_verifiedpermissions.types.claim.Claim"
    """<p>The token claim that you want Verified Permissions to interpret as group membership. For example, <code>groups</code>.</p>"""
    group_entity_type: (
        "aws_sdk_verifiedpermissions.types.group_entity_type.GroupEntityType"
    )
    """<p>The policy store entity type that you want to map your users' group claim to. For example, <code>MyCorp::UserGroup</code>. A group entity type is an entity that can have a user entity type as a member.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOpenIdConnectGroupConfiguration) -> dict:
    out: dict = {}
    out["groupClaim"] = value["group_claim"]
    out["groupEntityType"] = value["group_entity_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOpenIdConnectGroupConfiguration:
    out: UpdateOpenIdConnectGroupConfiguration = {}  # type: ignore[typeddict-item]
    if "groupClaim" in data:
        out["group_claim"] = data["groupClaim"]
    else:
        raise DeserializationError(
            "UpdateOpenIdConnectGroupConfiguration.group_claim required"
        )
    if "groupEntityType" in data:
        out["group_entity_type"] = data["groupEntityType"]
    else:
        raise DeserializationError(
            "UpdateOpenIdConnectGroupConfiguration.group_entity_type required"
        )
    return out
