"""Generated from Smithy shape ``com.amazonaws.controltower#ListBaselinesInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controltower.types.list_baselines_max_results


class ListBaselinesInput(TypedDict):
    next_token: NotRequired["str"]
    """<p>A pagination token.</p>"""
    max_results: NotRequired[
        "aws_sdk_controltower.types.list_baselines_max_results.ListBaselinesMaxResults"
    ]
    """<p>The maximum number of results to be shown.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBaselinesInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListBaselinesInput:
    out: ListBaselinesInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
