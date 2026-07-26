"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ListProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.profile_details


class ListProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>A token that indicates where the output should continue from, if a previous request did not show all results. To get the next results, make the request again with this value.</p>"""
    profiles: NotRequired["capo_rolesanywhere.types.profile_details.ProfileDetails"]
    """<p>A list of profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "profiles" in value:
        import capo_rolesanywhere.types.profile_details

        out["profiles"] = capo_rolesanywhere.types.profile_details.serialize_json(
            value["profiles"]
        )
    return out


def deserialize_json(data: dict) -> ListProfilesResponse:
    out: ListProfilesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "profiles" in data:
        import capo_rolesanywhere.types.profile_details

        out["profiles"] = capo_rolesanywhere.types.profile_details.deserialize_json(
            data["profiles"]
        )
    return out
