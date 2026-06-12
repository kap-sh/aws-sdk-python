"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfAggregatedLogOddsMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.aggregated_log_odds_metric

ListOfAggregatedLogOddsMetrics: TypeAlias = list[
    "aws_sdk_frauddetector.types.aggregated_log_odds_metric.AggregatedLogOddsMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfAggregatedLogOddsMetrics) -> list:
    import aws_sdk_frauddetector.types.aggregated_log_odds_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.aggregated_log_odds_metric.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfAggregatedLogOddsMetrics:
    import aws_sdk_frauddetector.types.aggregated_log_odds_metric

    out: ListOfAggregatedLogOddsMetrics = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.aggregated_log_odds_metric.deserialize_aws_json_1_1(
                item
            )
        )
    return out
