"""Generated from Smithy shape ``com.amazonaws.groundstation#ListMissionProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.mission_profile_list
    import capo_groundstation.types.pagination_token


class ListMissionProfilesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_groundstation.types.pagination_token.PaginationToken"]
    """<p>Next token returned in the response of a previous <code>ListMissionProfiles</code> call. Used to get the next page of results.</p>"""
    mission_profile_list: NotRequired[
        "capo_groundstation.types.mission_profile_list.MissionProfileList"
    ]
    """<p>List of mission profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMissionProfilesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "mission_profile_list" in value:
        import capo_groundstation.types.mission_profile_list

        out["missionProfileList"] = (
            capo_groundstation.types.mission_profile_list.serialize_json(
                value["mission_profile_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListMissionProfilesResponse:
    out: ListMissionProfilesResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "missionProfileList" in data:
        import capo_groundstation.types.mission_profile_list

        out["mission_profile_list"] = (
            capo_groundstation.types.mission_profile_list.deserialize_json(
                data["missionProfileList"]
            )
        )
    return out
