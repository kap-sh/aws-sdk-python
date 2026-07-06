"""Generated from Smithy shape ``com.amazonaws.rum#BatchCreateRumMetricDefinitionsError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rum.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rum.types.metric_definition_request


class BatchCreateRumMetricDefinitionsError(TypedDict, closed=True):
    metric_definition: (
        "aws_sdk_rum.types.metric_definition_request.MetricDefinitionRequest"
    )
    """<p>The metric definition that caused this error.</p>"""
    error_code: "str"
    """<p>The error code.</p>"""
    error_message: "str"
    """<p>The error message for this metric definition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRumMetricDefinitionsError) -> dict:
    out: dict = {}
    import aws_sdk_rum.types.metric_definition_request

    out["MetricDefinition"] = (
        aws_sdk_rum.types.metric_definition_request.serialize_json(
            value["metric_definition"]
        )
    )
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchCreateRumMetricDefinitionsError:
    out: BatchCreateRumMetricDefinitionsError = {}  # type: ignore[typeddict-item]
    if "MetricDefinition" in data:
        import aws_sdk_rum.types.metric_definition_request

        out["metric_definition"] = (
            aws_sdk_rum.types.metric_definition_request.deserialize_json(
                data["MetricDefinition"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsError.metric_definition required"
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsError.error_code required"
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    else:
        raise DeserializationError(
            "BatchCreateRumMetricDefinitionsError.error_message required"
        )
    return out
