"""Generated from Smithy shape ``com.amazonaws.rum#BatchDeleteRumMetricDefinitionsErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rum.types.batch_delete_rum_metric_definitions_error

BatchDeleteRumMetricDefinitionsErrors: TypeAlias = list[
    "capo_rum.types.batch_delete_rum_metric_definitions_error.BatchDeleteRumMetricDefinitionsError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteRumMetricDefinitionsErrors) -> list:
    import capo_rum.types.batch_delete_rum_metric_definitions_error

    out: list = []
    for item in value:
        out.append(
            capo_rum.types.batch_delete_rum_metric_definitions_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteRumMetricDefinitionsErrors:
    import capo_rum.types.batch_delete_rum_metric_definitions_error

    out: BatchDeleteRumMetricDefinitionsErrors = []
    for item in data:
        out.append(
            capo_rum.types.batch_delete_rum_metric_definitions_error.deserialize_json(
                item
            )
        )
    return out
