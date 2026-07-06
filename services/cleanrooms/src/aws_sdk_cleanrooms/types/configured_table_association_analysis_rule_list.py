"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfiguredTableAssociationAnalysisRuleList``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.allowed_additional_analyses
    import aws_sdk_cleanrooms.types.allowed_result_receivers


class ConfiguredTableAssociationAnalysisRuleList(TypedDict, closed=True):
    allowed_result_receivers: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_receivers.AllowedResultReceivers"
    ]
    """<p> The list of collaboration members who are allowed to receive results of queries run with this configured table.</p>"""
    allowed_additional_analyses: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    ]
    """<p> The list of resources or wildcards (ARNs) that are allowed to perform additional analysis on query output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredTableAssociationAnalysisRuleList) -> dict:
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


def deserialize_json(data: dict) -> ConfiguredTableAssociationAnalysisRuleList:
    out: ConfiguredTableAssociationAnalysisRuleList = {}  # type: ignore[typeddict-item]
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
