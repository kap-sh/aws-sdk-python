"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_trends_metrics_result

ResourcesTrendsMetrics: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_trends_metrics_result.ResourcesTrendsMetricsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsMetrics) -> list:
    import aws_sdk_securityhub.types.resources_trends_metrics_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.resources_trends_metrics_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourcesTrendsMetrics:
    import aws_sdk_securityhub.types.resources_trends_metrics_result

    out: ResourcesTrendsMetrics = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_trends_metrics_result.deserialize_json(
                item
            )
        )
    return out
