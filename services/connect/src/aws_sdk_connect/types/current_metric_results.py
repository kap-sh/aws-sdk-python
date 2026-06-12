"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric_result

CurrentMetricResults: TypeAlias = list[
    "aws_sdk_connect.types.current_metric_result.CurrentMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetricResults) -> list:
    import aws_sdk_connect.types.current_metric_result

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.current_metric_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrentMetricResults:
    import aws_sdk_connect.types.current_metric_result

    out: CurrentMetricResults = []
    for item in data:
        out.append(aws_sdk_connect.types.current_metric_result.deserialize_json(item))
    return out
