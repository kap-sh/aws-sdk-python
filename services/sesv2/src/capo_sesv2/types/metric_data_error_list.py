"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDataErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.metric_data_error

MetricDataErrorList: TypeAlias = list[
    "capo_sesv2.types.metric_data_error.MetricDataError"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataErrorList) -> list:
    import capo_sesv2.types.metric_data_error

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.metric_data_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDataErrorList:
    import capo_sesv2.types.metric_data_error

    out: MetricDataErrorList = []
    for item in data:
        out.append(capo_sesv2.types.metric_data_error.deserialize_json(item))
    return out
