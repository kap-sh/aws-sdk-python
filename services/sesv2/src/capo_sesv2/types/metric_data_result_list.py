"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDataResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.metric_data_result

MetricDataResultList: TypeAlias = list[
    "capo_sesv2.types.metric_data_result.MetricDataResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataResultList) -> list:
    import capo_sesv2.types.metric_data_result

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.metric_data_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDataResultList:
    import capo_sesv2.types.metric_data_result

    out: MetricDataResultList = []
    for item in data:
        out.append(capo_sesv2.types.metric_data_result.deserialize_json(item))
    return out
