"""Generated from Smithy shape ``com.amazonaws.datazone#LineageSqlQueryRunDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_datazone.types.failed_query_processing_error_messages


class LineageSqlQueryRunDetails(TypedDict, closed=True):
    query_start_time: NotRequired["datetime.datetime"]
    """<p>The query start time in the SQL query run details of a data lineage run.</p>"""
    query_end_time: NotRequired["datetime.datetime"]
    """<p>The query end time in the SQL query run details of a data lineage run.</p>"""
    total_queries_processed: NotRequired["int"]
    """<p>The total queries processed in the SQL query run details of a data lineage run.</p>"""
    num_queries_failed: NotRequired["int"]
    """<p>The number of queries that failed in the SQL query run details of a data lineage run.</p>"""
    error_messages: NotRequired[
        "capo_datazone.types.failed_query_processing_error_messages.FailedQueryProcessingErrorMessages"
    ]
    """<p>The error message of the SQL query run details of a data lineage run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageSqlQueryRunDetails) -> dict:
    out: dict = {}
    if "query_start_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["queryStartTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["query_start_time"]
        )
    if "query_end_time" in value:
        import capo_datazone.types._prelude.timestamp

        out["queryEndTime"] = capo_datazone.types._prelude.timestamp.serialize_json(
            value["query_end_time"]
        )
    if "total_queries_processed" in value:
        out["totalQueriesProcessed"] = value["total_queries_processed"]
    if "num_queries_failed" in value:
        out["numQueriesFailed"] = value["num_queries_failed"]
    if "error_messages" in value:
        import capo_datazone.types.failed_query_processing_error_messages

        out["errorMessages"] = (
            capo_datazone.types.failed_query_processing_error_messages.serialize_json(
                value["error_messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageSqlQueryRunDetails:
    out: LineageSqlQueryRunDetails = {}  # type: ignore[typeddict-item]
    if "queryStartTime" in data:
        import capo_datazone.types._prelude.timestamp

        out["query_start_time"] = (
            capo_datazone.types._prelude.timestamp.deserialize_json(
                data["queryStartTime"]
            )
        )
    if "queryEndTime" in data:
        import capo_datazone.types._prelude.timestamp

        out["query_end_time"] = capo_datazone.types._prelude.timestamp.deserialize_json(
            data["queryEndTime"]
        )
    if "totalQueriesProcessed" in data:
        out["total_queries_processed"] = data["totalQueriesProcessed"]
    if "numQueriesFailed" in data:
        out["num_queries_failed"] = data["numQueriesFailed"]
    if "errorMessages" in data:
        import capo_datazone.types.failed_query_processing_error_messages

        out["error_messages"] = (
            capo_datazone.types.failed_query_processing_error_messages.deserialize_json(
                data["errorMessages"]
            )
        )
    return out
