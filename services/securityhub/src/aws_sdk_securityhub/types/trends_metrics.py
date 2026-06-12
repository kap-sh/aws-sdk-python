"""Generated from Smithy shape ``com.amazonaws.securityhub#TrendsMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.trends_metrics_result

TrendsMetrics: TypeAlias = list[
    "aws_sdk_securityhub.types.trends_metrics_result.TrendsMetricsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrendsMetrics) -> list:
    import aws_sdk_securityhub.types.trends_metrics_result

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.trends_metrics_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrendsMetrics:
    import aws_sdk_securityhub.types.trends_metrics_result

    out: TrendsMetrics = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.trends_metrics_result.deserialize_json(item)
        )
    return out
