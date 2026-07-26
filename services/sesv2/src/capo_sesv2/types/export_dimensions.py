"""Generated from Smithy shape ``com.amazonaws.sesv2#ExportDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.export_dimension_value
    import capo_sesv2.types.metric_dimension_name

ExportDimensions: TypeAlias = dict[
    "capo_sesv2.types.metric_dimension_name.MetricDimensionName",
    "capo_sesv2.types.export_dimension_value.ExportDimensionValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExportDimensions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sesv2.types.export_dimension_value
        import capo_sesv2.types.metric_dimension_name

        out[capo_sesv2.types.metric_dimension_name.serialize_json(key)] = (
            capo_sesv2.types.export_dimension_value.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> ExportDimensions:
    out: ExportDimensions = {}
    for key, value in data.items():
        import capo_sesv2.types.export_dimension_value
        import capo_sesv2.types.metric_dimension_name

        out[capo_sesv2.types.metric_dimension_name.deserialize_json(key)] = (
            capo_sesv2.types.export_dimension_value.deserialize_json(value)
        )
    return out
