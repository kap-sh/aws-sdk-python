"""Generated from Smithy shape ``com.amazonaws.personalize#ListSolutionVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.next_token
    import aws_sdk_personalize.types.solution_versions


class ListSolutionVersionsResponse(TypedDict, closed=True):
    solution_versions: NotRequired[
        "aws_sdk_personalize.types.solution_versions.SolutionVersions"
    ]
    """<p>A list of solution versions describing the version properties.</p>"""
    next_token: NotRequired["aws_sdk_personalize.types.next_token.NextToken"]
    """<p>A token for getting the next set of solution versions (if they exist).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSolutionVersionsResponse) -> dict:
    out: dict = {}
    if "solution_versions" in value:
        import aws_sdk_personalize.types.solution_versions

        out["solutionVersions"] = (
            aws_sdk_personalize.types.solution_versions.serialize_aws_json_1_1(
                value["solution_versions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSolutionVersionsResponse:
    out: ListSolutionVersionsResponse = {}  # type: ignore[typeddict-item]
    if "solutionVersions" in data:
        import aws_sdk_personalize.types.solution_versions

        out["solution_versions"] = (
            aws_sdk_personalize.types.solution_versions.deserialize_aws_json_1_1(
                data["solutionVersions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
