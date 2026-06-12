"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetQueryStatisticsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.get_query_statistics_request_query_id_string


class GetQueryStatisticsRequest(TypedDict):
    query_id: "aws_sdk_lakeformation.types.get_query_statistics_request_query_id_string.GetQueryStatisticsRequestQueryIdString"
    """<p>The ID of the plan query operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatisticsRequest) -> dict:
    out: dict = {}
    out["QueryId"] = value["query_id"]
    return out


def deserialize_json(data: dict) -> GetQueryStatisticsRequest:
    out: GetQueryStatisticsRequest = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("GetQueryStatisticsRequest.query_id required")
    return out
