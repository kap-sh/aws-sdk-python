"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableImportanceMetrics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.list_of_log_odds_metrics


class VariableImportanceMetrics(TypedDict):
    log_odds_metrics: NotRequired[
        "aws_sdk_frauddetector.types.list_of_log_odds_metrics.ListOfLogOddsMetrics"
    ]
    """<p>List of variable metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableImportanceMetrics) -> dict:
    out: dict = {}
    if "log_odds_metrics" in value:
        import aws_sdk_frauddetector.types.list_of_log_odds_metrics

        out["logOddsMetrics"] = (
            aws_sdk_frauddetector.types.list_of_log_odds_metrics.serialize_aws_json_1_1(
                value["log_odds_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> VariableImportanceMetrics:
    out: VariableImportanceMetrics = {}  # type: ignore[typeddict-item]
    if "logOddsMetrics" in data:
        import aws_sdk_frauddetector.types.list_of_log_odds_metrics

        out["log_odds_metrics"] = (
            aws_sdk_frauddetector.types.list_of_log_odds_metrics.deserialize_aws_json_1_1(
                data["logOddsMetrics"]
            )
        )
    return out
