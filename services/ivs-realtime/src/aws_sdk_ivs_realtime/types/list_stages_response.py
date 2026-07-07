"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListStagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.pagination_token
    import aws_sdk_ivs_realtime.types.stage_summary_list


class ListStagesResponse(TypedDict, closed=True):
    stages: "aws_sdk_ivs_realtime.types.stage_summary_list.StageSummaryList"
    """<p>List of the matching stages (summary information only).</p>"""
    next_token: NotRequired[
        "aws_sdk_ivs_realtime.types.pagination_token.PaginationToken"
    ]
    """<p>If there are more stages than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStagesResponse) -> dict:
    out: dict = {}
    import aws_sdk_ivs_realtime.types.stage_summary_list

    out["stages"] = aws_sdk_ivs_realtime.types.stage_summary_list.serialize_json(
        value["stages"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStagesResponse:
    out: ListStagesResponse = {}  # type: ignore[typeddict-item]
    if "stages" in data:
        import aws_sdk_ivs_realtime.types.stage_summary_list

        out["stages"] = aws_sdk_ivs_realtime.types.stage_summary_list.deserialize_json(
            data["stages"]
        )
    else:
        raise DeserializationError("ListStagesResponse.stages required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
