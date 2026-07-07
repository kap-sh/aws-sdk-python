"""Generated from Smithy shape ``com.amazonaws.rum#BatchCreateRumMetricDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.batch_create_rum_metric_definitions_errors
    import aws_sdk_rum.types.metric_definitions


class BatchCreateRumMetricDefinitionsResponse(TypedDict, closed=True):
    errors: "aws_sdk_rum.types.batch_create_rum_metric_definitions_errors.BatchCreateRumMetricDefinitionsErrors"
    """<p>An array of error objects, if the operation caused any errors.</p>"""
    metric_definitions: NotRequired[
        "aws_sdk_rum.types.metric_definitions.MetricDefinitions"
    ]
    """<p>An array of structures that define the extended metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRumMetricDefinitionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_rum.types.batch_create_rum_metric_definitions_errors

    out["Errors"] = (
        aws_sdk_rum.types.batch_create_rum_metric_definitions_errors.serialize_json(
            value["errors"]
        )
    )
    if "metric_definitions" in value:
        import aws_sdk_rum.types.metric_definitions

        out["MetricDefinitions"] = aws_sdk_rum.types.metric_definitions.serialize_json(
            value["metric_definitions"]
        )
    return out


def deserialize_json(data: dict) -> BatchCreateRumMetricDefinitionsResponse:
    out: BatchCreateRumMetricDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_rum.types.batch_create_rum_metric_definitions_errors

        out["errors"] = (
            aws_sdk_rum.types.batch_create_rum_metric_definitions_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsResponse.errors required"
        )
    if "MetricDefinitions" in data:
        import aws_sdk_rum.types.metric_definitions

        out["metric_definitions"] = (
            aws_sdk_rum.types.metric_definitions.deserialize_json(
                data["MetricDefinitions"]
            )
        )
    return out
