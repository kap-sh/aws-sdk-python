"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListMemoriesInput``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ListMemoriesInput(TypedDict):
    max_results: "int"
    """<p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoriesInput) -> dict:
    out: dict = {}
    out["maxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoriesInput:
    out: ListMemoriesInput = {}  # type: ignore[typeddict-item]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
