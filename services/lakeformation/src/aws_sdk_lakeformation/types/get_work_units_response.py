"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetWorkUnitsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.query_id_string
    import aws_sdk_lakeformation.types.token
    import aws_sdk_lakeformation.types.work_unit_range_list


class GetWorkUnitsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.</p>"""
    query_id: "aws_sdk_lakeformation.types.query_id_string.QueryIdString"
    """<p>The ID of the plan query operation.</p>"""
    work_unit_ranges: (
        "aws_sdk_lakeformation.types.work_unit_range_list.WorkUnitRangeList"
    )
    """<p>A <code>WorkUnitRangeList</code> object that specifies the valid range of work unit IDs for querying the execution service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkUnitsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["QueryId"] = value["query_id"]
    import aws_sdk_lakeformation.types.work_unit_range_list

    out["WorkUnitRanges"] = (
        aws_sdk_lakeformation.types.work_unit_range_list.serialize_json(
            value["work_unit_ranges"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetWorkUnitsResponse:
    out: GetWorkUnitsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("GetWorkUnitsResponse.query_id required")
    if "WorkUnitRanges" in data:
        import aws_sdk_lakeformation.types.work_unit_range_list

        out["work_unit_ranges"] = (
            aws_sdk_lakeformation.types.work_unit_range_list.deserialize_json(
                data["WorkUnitRanges"]
            )
        )
    else:
        raise DeserializationError("GetWorkUnitsResponse.work_unit_ranges required")
    return out
