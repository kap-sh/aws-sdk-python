"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentTemplatesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.max_page_results
    import aws_sdk_proton.types.next_token


class ListEnvironmentTemplatesInput(TypedDict):
    next_token: NotRequired["aws_sdk_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next environment template in the array of environment templates, after the list of environment templates that was previously requested.</p>"""
    max_results: NotRequired["aws_sdk_proton.types.max_page_results.MaxPageResults"]
    """<p>The maximum number of environment templates to list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentTemplatesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentTemplatesInput:
    out: ListEnvironmentTemplatesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
