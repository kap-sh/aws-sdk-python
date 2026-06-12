"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDataResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.metric_data_result

MetricDataResultList: TypeAlias = list[
    "aws_sdk_sesv2.types.metric_data_result.MetricDataResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataResultList) -> list:
    import aws_sdk_sesv2.types.metric_data_result

    out: list = []
    for item in value:
        out.append(aws_sdk_sesv2.types.metric_data_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricDataResultList:
    import aws_sdk_sesv2.types.metric_data_result

    out: MetricDataResultList = []
    for item in data:
        out.append(aws_sdk_sesv2.types.metric_data_result.deserialize_json(item))
    return out
