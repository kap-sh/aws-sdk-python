"""Generated from Smithy shape ``com.amazonaws.connect#MetricResultsV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.metric_result_v2

MetricResultsV2: TypeAlias = list[
    "aws_sdk_connect.types.metric_result_v2.MetricResultV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricResultsV2) -> list:
    import aws_sdk_connect.types.metric_result_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.metric_result_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricResultsV2:
    import aws_sdk_connect.types.metric_result_v2

    out: MetricResultsV2 = []
    for item in data:
        out.append(aws_sdk_connect.types.metric_result_v2.deserialize_json(item))
    return out
