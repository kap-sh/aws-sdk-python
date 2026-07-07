"""Generated from Smithy shape ``com.amazonaws.iot#ListSecurityProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.next_token
    import aws_sdk_iot.types.security_profile_identifiers


class ListSecurityProfilesResponse(TypedDict, closed=True):
    security_profile_identifiers: NotRequired[
        "aws_sdk_iot.types.security_profile_identifiers.SecurityProfileIdentifiers"
    ]
    """<p>A list of security profile identifiers (names and ARNs).</p>"""
    next_token: NotRequired["aws_sdk_iot.types.next_token.NextToken"]
    """<p>A token that can be used to retrieve the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSecurityProfilesResponse) -> dict:
    out: dict = {}
    if "security_profile_identifiers" in value:
        import aws_sdk_iot.types.security_profile_identifiers

        out["securityProfileIdentifiers"] = (
            aws_sdk_iot.types.security_profile_identifiers.serialize_json(
                value["security_profile_identifiers"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSecurityProfilesResponse:
    out: ListSecurityProfilesResponse = {}  # type: ignore[typeddict-item]
    if "securityProfileIdentifiers" in data:
        import aws_sdk_iot.types.security_profile_identifiers

        out["security_profile_identifiers"] = (
            aws_sdk_iot.types.security_profile_identifiers.deserialize_json(
                data["securityProfileIdentifiers"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
