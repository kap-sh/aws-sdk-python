"""Generated from Smithy shape ``com.amazonaws.sesv2#BatchGetMetricDataResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.metric_data_error_list
    import aws_sdk_sesv2.types.metric_data_result_list


class BatchGetMetricDataResponse(TypedDict):
    results: NotRequired[
        "aws_sdk_sesv2.types.metric_data_result_list.MetricDataResultList"
    ]
    """<p>A list of successfully retrieved <code>MetricDataResult</code>.</p>"""
    errors: NotRequired[
        "aws_sdk_sesv2.types.metric_data_error_list.MetricDataErrorList"
    ]
    """<p>A list of <code>MetricDataError</code> encountered while processing your metric data batch request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricDataResponse) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_sesv2.types.metric_data_result_list

        out["Results"] = aws_sdk_sesv2.types.metric_data_result_list.serialize_json(
            value["results"]
        )
    if "errors" in value:
        import aws_sdk_sesv2.types.metric_data_error_list

        out["Errors"] = aws_sdk_sesv2.types.metric_data_error_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetMetricDataResponse:
    out: BatchGetMetricDataResponse = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_sesv2.types.metric_data_result_list

        out["results"] = aws_sdk_sesv2.types.metric_data_result_list.deserialize_json(
            data["Results"]
        )
    if "Errors" in data:
        import aws_sdk_sesv2.types.metric_data_error_list

        out["errors"] = aws_sdk_sesv2.types.metric_data_error_list.deserialize_json(
            data["Errors"]
        )
    return out
