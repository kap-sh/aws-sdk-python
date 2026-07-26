"""Generated from Smithy shape ``com.amazonaws.rum#BatchCreateRumMetricDefinitionsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.batch_create_rum_metric_definitions_error

BatchCreateRumMetricDefinitionsErrors: TypeAlias = list[
    "capo_rum.types.batch_create_rum_metric_definitions_error.BatchCreateRumMetricDefinitionsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRumMetricDefinitionsErrors) -> list:
    import capo_rum.types.batch_create_rum_metric_definitions_error

    out: list = []
    for item in value:
        out.append(
            capo_rum.types.batch_create_rum_metric_definitions_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateRumMetricDefinitionsErrors:
    import capo_rum.types.batch_create_rum_metric_definitions_error

    out: BatchCreateRumMetricDefinitionsErrors = []
    for item in data:
        out.append(
            capo_rum.types.batch_create_rum_metric_definitions_error.deserialize_json(
                item
            )
        )
    return out
