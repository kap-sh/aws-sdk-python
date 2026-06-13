"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors
    import aws_sdk_rum.types.metric_definition_ids


class BatchDeleteRumMetricDefinitionsResponse(TypedDict):
    errors: "aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors.BatchDeleteRumMetricDefinitionsErrors"
    """<p>An array of error objects, if the operation caused any errors.</p>"""
    metric_definition_ids: NotRequired[
        "aws_sdk_rum.types.metric_definition_ids.MetricDefinitionIds"
    ]
    """<p>The IDs of the metric definitions that were deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRumMetricDefinitionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors

    out["Errors"] = (
        aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors.serialize_json(
            value["errors"]
        )
    )
    if "metric_definition_ids" in value:
        import aws_sdk_rum.types.metric_definition_ids

        out["MetricDefinitionIds"] = (
            aws_sdk_rum.types.metric_definition_ids.serialize_json(
                value["metric_definition_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteRumMetricDefinitionsResponse:
    out: BatchDeleteRumMetricDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors

        out["errors"] = (
            aws_sdk_rum.types.batch_delete_rum_metric_definitions_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDeleteRumMetricDefinitionsResponse.errors required"
        )
    if "MetricDefinitionIds" in data:
        import aws_sdk_rum.types.metric_definition_ids

        out["metric_definition_ids"] = (
            aws_sdk_rum.types.metric_definition_ids.deserialize_json(
                data["MetricDefinitionIds"]
            )
        )
    return out
