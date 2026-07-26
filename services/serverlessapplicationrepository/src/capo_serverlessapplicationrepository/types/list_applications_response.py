"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of_application_summary
    import capo_serverlessapplicationrepository.types.__string


class ListApplicationsResponse(TypedDict, closed=True):
    applications: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_application_summary.__listOfApplicationSummary"
    ]
    """<p>An array of application summaries.</p>"""
    next_token: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_serverlessapplicationrepository.types.__list_of_application_summary

        out["applications"] = (
            capo_serverlessapplicationrepository.types.__list_of_application_summary.serialize_json(
                value["applications"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "applications" in data:
        import capo_serverlessapplicationrepository.types.__list_of_application_summary

        out["applications"] = (
            capo_serverlessapplicationrepository.types.__list_of_application_summary.deserialize_json(
                data["applications"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
