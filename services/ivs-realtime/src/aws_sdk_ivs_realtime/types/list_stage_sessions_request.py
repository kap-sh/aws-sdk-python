"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStageSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.max_stage_session_results
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.stage_arn


class ListStageSessionsRequest(TypedDict, closed=True):
    stage_arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>The first stage session to retrieve. This is used for pagination; see the <code>nextToken</code> response field.</p>"""
    max_results: NotRequired[
        "aws_sdk_ivs_realtime.types.max_stage_session_results.MaxStageSessionResults"
    ]
    """<p>Maximum number of results to return. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStageSessionsRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListStageSessionsRequest:
    out: ListStageSessionsRequest = {}  # type: ignore[typeddict-item]
    if "stageArn" in data:
        out["stage_arn"] = data["stageArn"]
    else:
        raise DeserializationError("ListStageSessionsRequest.stage_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
