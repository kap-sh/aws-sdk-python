"""Generated from Smithy shape ``com.amazonaws.connect#ContactMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_metric_info

ContactMetrics: TypeAlias = list[
    "aws_sdk_connect.types.contact_metric_info.ContactMetricInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactMetrics) -> list:
    import aws_sdk_connect.types.contact_metric_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_metric_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactMetrics:
    import aws_sdk_connect.types.contact_metric_info

    out: ContactMetrics = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_metric_info.deserialize_json(item))
    return out
