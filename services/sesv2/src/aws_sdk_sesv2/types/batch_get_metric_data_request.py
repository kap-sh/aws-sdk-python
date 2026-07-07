"""Generated from Smithy shape ``com.amazonaws.sesv2#BatchGetMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.batch_get_metric_data_queries


class BatchGetMetricDataRequest(TypedDict, closed=True):
    queries: (
        "aws_sdk_sesv2.types.batch_get_metric_data_queries.BatchGetMetricDataQueries"
    )
    """<p>A list of queries for metrics to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricDataRequest) -> dict:
    out: dict = {}
    import aws_sdk_sesv2.types.batch_get_metric_data_queries

    out["Queries"] = aws_sdk_sesv2.types.batch_get_metric_data_queries.serialize_json(
        value["queries"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetMetricDataRequest:
    out: BatchGetMetricDataRequest = {}  # type: ignore[typeddict-item]
    if "Queries" in data:
        import aws_sdk_sesv2.types.batch_get_metric_data_queries

        out["queries"] = (
            aws_sdk_sesv2.types.batch_get_metric_data_queries.deserialize_json(
                data["Queries"]
            )
        )
    else:
        raise DeserializationError("BatchGetMetricDataRequest.queries required")
    return out
