"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportDimensionValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.metric_dimension_value

ExportDimensionValue: TypeAlias = list[
    "capo_sesv2.types.metric_dimension_value.MetricDimensionValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportDimensionValue) -> list:
    return list(value)


def deserialize_json(data: list) -> ExportDimensionValue:
    return list(data)
