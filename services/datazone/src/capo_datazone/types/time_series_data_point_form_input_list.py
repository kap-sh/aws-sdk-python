"""Generated from Smithy shape ``com.amazonaws.datazone#TimeSeriesDataPointFormInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.time_series_data_point_form_input

TimeSeriesDataPointFormInputList: TypeAlias = list[
    "capo_datazone.types.time_series_data_point_form_input.TimeSeriesDataPointFormInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: TimeSeriesDataPointFormInputList) -> list:
    import capo_datazone.types.time_series_data_point_form_input

    out: list = []
    for item in value:
        out.append(
            capo_datazone.types.time_series_data_point_form_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TimeSeriesDataPointFormInputList:
    import capo_datazone.types.time_series_data_point_form_input

    out: TimeSeriesDataPointFormInputList = []
    for item in data:
        out.append(
            capo_datazone.types.time_series_data_point_form_input.deserialize_json(item)
        )
    return out
