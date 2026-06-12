"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationVersionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary
    import aws_sdk_serverlessapplicationrepository.types.__string


class ListApplicationVersionsResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The token to request the next page of results.</p>"""
    versions: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary.__listOfVersionSummary"
    ]
    """<p>An array of version summaries for the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationVersionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "versions" in value:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary

        out["versions"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary.serialize_json(
                value["versions"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListApplicationVersionsResponse:
    out: ListApplicationVersionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "versions" in data:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary

        out["versions"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_version_summary.deserialize_json(
                data["versions"]
            )
        )
    return out
