"""Generated from Smithy shape ``com.amazonaws.datazone#LineageSqlQueryRunDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_datazone.types.failed_query_processing_error_messages


class LineageSqlQueryRunDetails(TypedDict):
    query_start_time: NotRequired["datetime.datetime"]
    """<p>The query start time in the SQL query run details of a data lineage run.</p>"""
    query_end_time: NotRequired["datetime.datetime"]
    """<p>The query end time in the SQL query run details of a data lineage run.</p>"""
    total_queries_processed: NotRequired["int"]
    """<p>The total queries processed in the SQL query run details of a data lineage run.</p>"""
    num_queries_failed: NotRequired["int"]
    """<p>The number of queries that failed in the SQL query run details of a data lineage run.</p>"""
    error_messages: NotRequired[
        "aws_sdk_datazone.types.failed_query_processing_error_messages.FailedQueryProcessingErrorMessages"
    ]
    """<p>The error message of the SQL query run details of a data lineage run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageSqlQueryRunDetails) -> dict:
    out: dict = {}
    if "query_start_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["queryStartTime"] = (
            aws_sdk_datazone.types._prelude.timestamp.serialize_json(
                value["query_start_time"]
            )
        )
    if "query_end_time" in value:
        import aws_sdk_datazone.types._prelude.timestamp

        out["queryEndTime"] = aws_sdk_datazone.types._prelude.timestamp.serialize_json(
            value["query_end_time"]
        )
    if "total_queries_processed" in value:
        out["totalQueriesProcessed"] = value["total_queries_processed"]
    if "num_queries_failed" in value:
        out["numQueriesFailed"] = value["num_queries_failed"]
    if "error_messages" in value:
        import aws_sdk_datazone.types.failed_query_processing_error_messages

        out["errorMessages"] = (
            aws_sdk_datazone.types.failed_query_processing_error_messages.serialize_json(
                value["error_messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> LineageSqlQueryRunDetails:
    out: LineageSqlQueryRunDetails = {}  # type: ignore[typeddict-item]
    if "queryStartTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["query_start_time"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["queryStartTime"]
            )
        )
    if "queryEndTime" in data:
        import aws_sdk_datazone.types._prelude.timestamp

        out["query_end_time"] = (
            aws_sdk_datazone.types._prelude.timestamp.deserialize_json(
                data["queryEndTime"]
            )
        )
    if "totalQueriesProcessed" in data:
        out["total_queries_processed"] = data["totalQueriesProcessed"]
    if "numQueriesFailed" in data:
        out["num_queries_failed"] = data["numQueriesFailed"]
    if "errorMessages" in data:
        import aws_sdk_datazone.types.failed_query_processing_error_messages

        out["error_messages"] = (
            aws_sdk_datazone.types.failed_query_processing_error_messages.deserialize_json(
                data["errorMessages"]
            )
        )
    return out
