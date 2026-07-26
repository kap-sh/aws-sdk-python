"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScheduledQueryInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.long
    import capo_timestream_query.types.query_spatial_coverage
    import capo_timestream_query.types.query_temporal_range


class ScheduledQueryInsightsResponse(TypedDict, closed=True):
    query_spatial_coverage: NotRequired[
        "capo_timestream_query.types.query_spatial_coverage.QuerySpatialCoverage"
    ]
    """<p>Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.</p>"""
    query_temporal_range: NotRequired[
        "capo_timestream_query.types.query_temporal_range.QueryTemporalRange"
    ]
    """<p>Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:</p> <ul> <li> <p>Add missing time-predicates.</p> </li> <li> <p>Remove functions around the time predicates.</p> </li> <li> <p>Add time predicates to all the sub-queries.</p> </li> </ul>"""
    query_table_count: NotRequired["capo_timestream_query.types.long.Long"]
    """<p>Indicates the number of tables in the query.</p>"""
    output_rows: NotRequired["capo_timestream_query.types.long.Long"]
    """<p>Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.</p>"""
    output_bytes: NotRequired["capo_timestream_query.types.long.Long"]
    """<p>Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScheduledQueryInsightsResponse) -> dict:
    out: dict = {}
    if "query_spatial_coverage" in value:
        import capo_timestream_query.types.query_spatial_coverage

        out["QuerySpatialCoverage"] = (
            capo_timestream_query.types.query_spatial_coverage.serialize_aws_json_1_0(
                value["query_spatial_coverage"]
            )
        )
    if "query_temporal_range" in value:
        import capo_timestream_query.types.query_temporal_range

        out["QueryTemporalRange"] = (
            capo_timestream_query.types.query_temporal_range.serialize_aws_json_1_0(
                value["query_temporal_range"]
            )
        )
    if "query_table_count" in value:
        out["QueryTableCount"] = value["query_table_count"]
    if "output_rows" in value:
        out["OutputRows"] = value["output_rows"]
    if "output_bytes" in value:
        out["OutputBytes"] = value["output_bytes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ScheduledQueryInsightsResponse:
    out: ScheduledQueryInsightsResponse = {}  # type: ignore[typeddict-item]
    if "QuerySpatialCoverage" in data:
        import capo_timestream_query.types.query_spatial_coverage

        out["query_spatial_coverage"] = (
            capo_timestream_query.types.query_spatial_coverage.deserialize_aws_json_1_0(
                data["QuerySpatialCoverage"]
            )
        )
    if "QueryTemporalRange" in data:
        import capo_timestream_query.types.query_temporal_range

        out["query_temporal_range"] = (
            capo_timestream_query.types.query_temporal_range.deserialize_aws_json_1_0(
                data["QueryTemporalRange"]
            )
        )
    if "QueryTableCount" in data:
        out["query_table_count"] = data["QueryTableCount"]
    if "OutputRows" in data:
        out["output_rows"] = data["OutputRows"]
    if "OutputBytes" in data:
        out["output_bytes"] = data["OutputBytes"]
    return out
