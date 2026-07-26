"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskRunsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.database_name
    import capo_glue.types.name_string
    import capo_glue.types.page_size
    import capo_glue.types.token


class GetColumnStatisticsTaskRunsRequest(TypedDict, closed=True):
    database_name: "capo_glue.types.database_name.DatabaseName"
    """<p>The name of the database where the table resides.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    max_results: NotRequired["capo_glue.types.page_size.PageSize"]
    """<p>The maximum size of the response.</p>"""
    next_token: NotRequired["capo_glue.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskRunsRequest) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskRunsRequest:
    out: GetColumnStatisticsTaskRunsRequest = {}  # type: ignore[typeddict-item]
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsTaskRunsRequest.database_name required"
        )
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError(
            "GetColumnStatisticsTaskRunsRequest.table_name required"
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
