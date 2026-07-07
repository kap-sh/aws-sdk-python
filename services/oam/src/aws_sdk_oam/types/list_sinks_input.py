"""Generated from Smithy shape ``com.amazonaws.oam#ListSinksInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_oam.types.list_sinks_max_results
    import aws_sdk_oam.types.next_token


class ListSinksInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_oam.types.list_sinks_max_results.ListSinksMaxResults"
    ]
    """<p>Limits the number of returned links to the specified number.</p>"""
    next_token: NotRequired["aws_sdk_oam.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. You received this token from a previous call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSinksInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListSinksInput:
    out: ListSinksInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
