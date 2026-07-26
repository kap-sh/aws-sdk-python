"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableImportanceMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.list_of_log_odds_metrics


class VariableImportanceMetrics(TypedDict, closed=True):
    log_odds_metrics: NotRequired[
        "capo_frauddetector.types.list_of_log_odds_metrics.ListOfLogOddsMetrics"
    ]
    """<p>List of variable metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableImportanceMetrics) -> dict:
    out: dict = {}
    if "log_odds_metrics" in value:
        import capo_frauddetector.types.list_of_log_odds_metrics

        out["logOddsMetrics"] = (
            capo_frauddetector.types.list_of_log_odds_metrics.serialize_aws_json_1_1(
                value["log_odds_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VariableImportanceMetrics:
    out: VariableImportanceMetrics = {}  # type: ignore[typeddict-item]
    if "logOddsMetrics" in data:
        import capo_frauddetector.types.list_of_log_odds_metrics

        out["log_odds_metrics"] = (
            capo_frauddetector.types.list_of_log_odds_metrics.deserialize_aws_json_1_1(
                data["logOddsMetrics"]
            )
        )
    return out
