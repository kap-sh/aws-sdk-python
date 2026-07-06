"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.max_stage_results
    import aws_sdk_ivs_realtime.types.pagination_token


class ListStagesRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first stage to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_stage_results.MaxStageResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStagesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListStagesRequest:
    out: ListStagesRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
