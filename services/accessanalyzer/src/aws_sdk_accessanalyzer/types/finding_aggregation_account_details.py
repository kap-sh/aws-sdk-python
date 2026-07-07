"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingAggregationAccountDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map


class FindingAggregationAccountDetails(TypedDict, closed=True):
    account: NotRequired["str"]
    """<p>The ID of the Amazon Web Services account for which unused access finding details are provided.</p>"""
    number_of_active_findings: NotRequired["int"]
    """<p>The number of active unused access findings for the specified Amazon Web Services account.</p>"""
    details: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map.FindingAggregationAccountDetailsMap"
    ]
    """<p>Provides the number of active findings for each type of unused access for the specified Amazon Web Services account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingAggregationAccountDetails) -> dict:
    out: dict = {}
    if "account" in value:
        out["account"] = value["account"]
    if "number_of_active_findings" in value:
        out["numberOfActiveFindings"] = value["number_of_active_findings"]
    if "details" in value:
        import aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map

        out["details"] = (
            aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map.serialize_json(
                value["details"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingAggregationAccountDetails:
    out: FindingAggregationAccountDetails = {}  # type: ignore[typeddict-item]
    if "account" in data:
        out["account"] = data["account"]
    if "numberOfActiveFindings" in data:
        out["number_of_active_findings"] = data["numberOfActiveFindings"]
    if "details" in data:
        import aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map

        out["details"] = (
            aws_sdk_accessanalyzer.types.finding_aggregation_account_details_map.deserialize_json(
                data["details"]
            )
        )
    return out
