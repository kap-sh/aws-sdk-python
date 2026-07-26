"""Generated from Smithy shape ``com.amazonaws.connect#ListAuthenticationProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.authentication_profile_summary_list
    import capo_connect.types.next_token


class ListAuthenticationProfilesResponse(TypedDict, closed=True):
    authentication_profile_summary_list: NotRequired[
        "capo_connect.types.authentication_profile_summary_list.AuthenticationProfileSummaryList"
    ]
    """<p>A summary of a given authentication profile.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuthenticationProfilesResponse) -> dict:
    out: dict = {}
    if "authentication_profile_summary_list" in value:
        import capo_connect.types.authentication_profile_summary_list

        out["AuthenticationProfileSummaryList"] = (
            capo_connect.types.authentication_profile_summary_list.serialize_json(
                value["authentication_profile_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAuthenticationProfilesResponse:
    out: ListAuthenticationProfilesResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationProfileSummaryList" in data:
        import capo_connect.types.authentication_profile_summary_list

        out["authentication_profile_summary_list"] = (
            capo_connect.types.authentication_profile_summary_list.deserialize_json(
                data["AuthenticationProfileSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
