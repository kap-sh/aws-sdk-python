"""Generated from Smithy shape ``com.amazonaws.iot#ListSecurityProfilesForTargetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.security_profile_target_mappings


class ListSecurityProfilesForTargetResponse(TypedDict):
    security_profile_target_mappings: NotRequired[
        "aws_sdk_iot.types.security_profile_target_mappings.SecurityProfileTargetMappings"
    ]
    """<p>A list of security profiles and their associated targets.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesForTargetResponse) -> dict:
    out: dict = {}
    if "security_profile_target_mappings" in value:
        import aws_sdk_iot.types.security_profile_target_mappings

        out["securityProfileTargetMappings"] = (
            aws_sdk_iot.types.security_profile_target_mappings.serialize_json(
                value["security_profile_target_mappings"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesForTargetResponse:
    out: ListSecurityProfilesForTargetResponse = {}  # type: ignore[typeddict-item]
    if "securityProfileTargetMappings" in data:
        import aws_sdk_iot.types.security_profile_target_mappings

        out["security_profile_target_mappings"] = (
            aws_sdk_iot.types.security_profile_target_mappings.deserialize_json(
                data["securityProfileTargetMappings"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
