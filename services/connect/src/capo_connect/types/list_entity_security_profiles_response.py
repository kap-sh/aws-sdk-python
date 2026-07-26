"""Generated from Smithy shape ``com.amazonaws.connect#ListEntitySecurityProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token2500
    import capo_connect.types.security_profiles100


class ListEntitySecurityProfilesResponse(TypedDict, closed=True):
    security_profiles: NotRequired[
        "capo_connect.types.security_profiles100.SecurityProfiles100"
    ]
    """<p> List of Security Profile Object. </p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p> The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitySecurityProfilesResponse) -> dict:
    out: dict = {}
    if "security_profiles" in value:
        import capo_connect.types.security_profiles100

        out["SecurityProfiles"] = (
            capo_connect.types.security_profiles100.serialize_json(
                value["security_profiles"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEntitySecurityProfilesResponse:
    out: ListEntitySecurityProfilesResponse = {}  # type: ignore[typeddict-item]
    if "SecurityProfiles" in data:
        import capo_connect.types.security_profiles100

        out["security_profiles"] = (
            capo_connect.types.security_profiles100.deserialize_json(
                data["SecurityProfiles"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
