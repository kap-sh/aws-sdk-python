"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ListApplicationDependenciesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary
    import aws_sdk_serverlessapplicationrepository.types.__string


class ListApplicationDependenciesResponse(TypedDict):
    dependencies: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary.__listOfApplicationDependencySummary"
    ]
    """<p>An array of application summaries nested in the application.</p>"""
    next_token: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The token to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationDependenciesResponse) -> dict:
    out: dict = {}
    if "dependencies" in value:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary

        out["dependencies"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary.serialize_json(
                value["dependencies"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationDependenciesResponse:
    out: ListApplicationDependenciesResponse = {}  # type: ignore[typeddict-item]
    if "dependencies" in data:
        import aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary

        out["dependencies"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of_application_dependency_summary.deserialize_json(
                data["dependencies"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
