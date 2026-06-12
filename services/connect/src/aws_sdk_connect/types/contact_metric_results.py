"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetricResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_metric_result

ContactMetricResults: TypeAlias = list[
    "aws_sdk_connect.types.contact_metric_result.ContactMetricResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetricResults) -> list:
    import aws_sdk_connect.types.contact_metric_result

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_metric_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactMetricResults:
    import aws_sdk_connect.types.contact_metric_result

    out: ContactMetricResults = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_metric_result.deserialize_json(item))
    return out
