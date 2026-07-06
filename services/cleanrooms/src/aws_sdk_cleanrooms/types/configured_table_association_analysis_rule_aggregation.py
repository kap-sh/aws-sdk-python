"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRuleAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.allowed_additional_analyses
    import aws_sdk_cleanrooms.types.allowed_result_receivers


class ConfiguredTableAssociationAnalysisRuleAggregation(TypedDict, closed=True):
    allowed_result_receivers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p> The list of collaboration members who are allowed to receive results of queries run with this configured table.</p>"""
    allowed_additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p> The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.</p> <p>The <code>allowedAdditionalAnalyses</code> parameter is currently supported for the list analysis rule (<code>AnalysisRuleList</code>) and the custom analysis rule (<code>AnalysisRuleCustom</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRuleAggregation) -> dict:
    out: dict = {}
    if "allowed_result_receivers" in value:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowedResultReceivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.serialize_json(
                value["allowed_result_receivers"]
            )
        )
    if "allowed_additional_analyses" in value:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowedAdditionalAnalyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.serialize_json(
                value["allowed_additional_analyses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRuleAggregation:
    out: ConfiguredTableAssociationAnalysisRuleAggregation = {}  # type: ignore[typeddict-item]
    if "allowedResultReceivers" in data:
        import aws_sdk_cleanrooms.types.allowed_result_receivers

        out["allowed_result_receivers"] = (
            aws_sdk_cleanrooms.types.allowed_result_receivers.deserialize_json(
                data["allowedResultReceivers"]
            )
        )
    if "allowedAdditionalAnalyses" in data:
        import aws_sdk_cleanrooms.types.allowed_additional_analyses

        out["allowed_additional_analyses"] = (
            aws_sdk_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["allowedAdditionalAnalyses"]
            )
        )
    return out
