"""Generated from Smithy shape ``com.amazonaws.connect#ListEntitySecurityProfilesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.next_token2500
    import aws_sdk_connect.types.security_profiles100


class ListEntitySecurityProfilesResponse(TypedDict):
    security_profiles: NotRequired[
        "aws_sdk_connect.types.security_profiles100.SecurityProfiles100"
    ]
    """<p> List of Security Profile Object. </p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token2500.NextToken2500"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitySecurityProfilesResponse) -> dict:
    out: dict = {}
    if "security_profiles" in value:
        import aws_sdk_connect.types.security_profiles100

        out["SecurityProfiles"] = (
            aws_sdk_connect.types.security_profiles100.serialize_json(
                value["security_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitySecurityProfilesResponse:
    out: ListEntitySecurityProfilesResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfiles" in data:
        import aws_sdk_connect.types.security_profiles100

        out["security_profiles"] = (
            aws_sdk_connect.types.security_profiles100.deserialize_json(
                data["SecurityProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
