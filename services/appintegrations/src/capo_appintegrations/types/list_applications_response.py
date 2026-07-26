"""Generated from Smithy shape ``com.amazonaws.appintegrations#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.applications_list
    import capo_appintegrations.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    applications: NotRequired[
        "capo_appintegrations.types.applications_list.ApplicationsList"
    ]
    """<p>The Applications associated with this account.</p>"""
    next_token: NotRequired["capo_appintegrations.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_appintegrations.types.applications_list

        out["Applications"] = (
            capo_appintegrations.types.applications_list.serialize_json(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "Applications" in data:
        import capo_appintegrations.types.applications_list

        out["applications"] = (
            capo_appintegrations.types.applications_list.deserialize_json(
                data["Applications"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
