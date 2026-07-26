"""Generated from Smithy shape ``com.amazonaws.securityhub#TrendsMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.trends_metrics_result

TrendsMetrics: TypeAlias = list[
    "capo_securityhub.types.trends_metrics_result.TrendsMetricsResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrendsMetrics) -> list:
    import capo_securityhub.types.trends_metrics_result

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.trends_metrics_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> TrendsMetrics:
    import capo_securityhub.types.trends_metrics_result

    out: TrendsMetrics = []
    for item in data:
        out.append(capo_securityhub.types.trends_metrics_result.deserialize_json(item))
    return out
