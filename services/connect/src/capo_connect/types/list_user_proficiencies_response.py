"""Generated from Smithy shape ``com.amazonaws.connect#ListUserProficienciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.region_name
    import capo_connect.types.timestamp
    import capo_connect.types.user_proficiency_list


class ListUserProficienciesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""
    user_proficiency_list: NotRequired[
        "capo_connect.types.user_proficiency_list.UserProficiencyList"
    ]
    """<p>Information about the user proficiencies.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The last time that the user's proficiencies are were modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region in which a user's proficiencies were last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserProficienciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "user_proficiency_list" in value:
        import capo_connect.types.user_proficiency_list

        out["UserProficiencyList"] = (
            capo_connect.types.user_proficiency_list.serialize_json(
                value["user_proficiency_list"]
            )
        )
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> ListUserProficienciesResponse:
    out: ListUserProficienciesResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "UserProficiencyList" in data:
        import capo_connect.types.user_proficiency_list

        out["user_proficiency_list"] = (
            capo_connect.types.user_proficiency_list.deserialize_json(
                data["UserProficiencyList"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
