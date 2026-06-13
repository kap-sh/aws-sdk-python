"""Generated from Smithy shape ``com.amazonaws.proton#ListRepositoriesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token


class ListRepositoriesInput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next repository in the array of repositories, after the list of repositories previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of repositories to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRepositoriesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRepositoriesInput:
    out: ListRepositoriesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
