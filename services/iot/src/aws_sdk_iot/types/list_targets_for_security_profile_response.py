"""Generated from Smithy shape ``com.amazonaws.iot#ListTargetsForSecurityProfileResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.security_profile_targets


class ListTargetsForSecurityProfileResponse(TypedDict):
    security_profile_targets: NotRequired[
        "aws_sdk_iot.types.security_profile_targets.SecurityProfileTargets"
    ]
    """<p>The thing groups to which the security profile is attached.</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTargetsForSecurityProfileResponse) -> dict:
    out: dict = {}
    if "security_profile_targets" in value:
        import aws_sdk_iot.types.security_profile_targets

        out["securityProfileTargets"] = (
            aws_sdk_iot.types.security_profile_targets.serialize_json(
                value["security_profile_targets"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTargetsForSecurityProfileResponse:
    out: ListTargetsForSecurityProfileResponse = {}  # type: ignore[typeddict-item]
    if "securityProfileTargets" in data:
        import aws_sdk_iot.types.security_profile_targets

        out["security_profile_targets"] = (
            aws_sdk_iot.types.security_profile_targets.deserialize_json(
                data["securityProfileTargets"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
