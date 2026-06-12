"""Generated from Smithy shape ``com.amazonaws.frauddetector#AggregatedVariablesImportanceMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics


class AggregatedVariablesImportanceMetrics(TypedDict):
    log_odds_metrics: NotRequired[
        "aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics.ListOfAggregatedLogOddsMetrics"
    ]
    """<p> List of variables' metrics. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedVariablesImportanceMetrics) -> dict:
    out: dict = {}
    if "log_odds_metrics" in value:
        import aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics

        out["logOddsMetrics"] = (
            aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics.serialize_aws_json_1_1(
                value["log_odds_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatedVariablesImportanceMetrics:
    out: AggregatedVariablesImportanceMetrics = {}  # type: ignore[typeddict-item]
    if "logOddsMetrics" in data:
        import aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics

        out["log_odds_metrics"] = (
            aws_sdk_frauddetector.types.list_of_aggregated_log_odds_metrics.deserialize_aws_json_1_1(
                data["logOddsMetrics"]
            )
        )
    return out
