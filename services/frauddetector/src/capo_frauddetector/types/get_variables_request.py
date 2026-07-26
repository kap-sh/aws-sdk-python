"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetVariablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.string
    import capo_frauddetector.types.variables_max_results


class GetVariablesRequest(TypedDict, closed=True):
    name: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The name of the variable. </p>"""
    next_token: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The next page token of the get variable request. </p>"""
    max_results: NotRequired[
        "capo_frauddetector.types.variables_max_results.VariablesMaxResults"
    ]
    """<p>The max size per page determined for the get variable request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetVariablesRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetVariablesRequest:
    out: GetVariablesRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
