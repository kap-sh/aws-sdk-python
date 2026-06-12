"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfLogOddsMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.log_odds_metric

ListOfLogOddsMetrics: TypeAlias = list[
    "aws_sdk_frauddetector.types.log_odds_metric.LogOddsMetric"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfLogOddsMetrics) -> list:
    import aws_sdk_frauddetector.types.log_odds_metric

    out: list = []
    for item in value:
        out.append(
            aws_sdk_frauddetector.types.log_odds_metric.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfLogOddsMetrics:
    import aws_sdk_frauddetector.types.log_odds_metric

    out: ListOfLogOddsMetrics = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.log_odds_metric.deserialize_aws_json_1_1(item)
        )
    return out
