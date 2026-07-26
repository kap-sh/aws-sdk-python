"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__list_of_version_summary
    import capo_serverlessapplicationrepository.types.__string


class ListApplicationVersionsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The token to request the next page of results.</p>"""
    versions: NotRequired[
        "capo_serverlessapplicationrepository.types.__list_of_version_summary.__listOfVersionSummary"
    ]
    """<p>An array of version summaries for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "versions" in value:
        import capo_serverlessapplicationrepository.types.__list_of_version_summary

        out["versions"] = (
            capo_serverlessapplicationrepository.types.__list_of_version_summary.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsResponse:
    out: ListApplicationVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "versions" in data:
        import capo_serverlessapplicationrepository.types.__list_of_version_summary

        out["versions"] = (
            capo_serverlessapplicationrepository.types.__list_of_version_summary.deserialize_json(
                data["versions"]
            )
        )
    return out
