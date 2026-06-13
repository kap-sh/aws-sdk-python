"""Generated from Smithy shape ``com.amazonaws.inspector2#FindingTypeAggregationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.severity_counts


class FindingTypeAggregationResponse(TypedDict):
    account_id: NotRequired["aws_sdk_inspector2.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the findings.</p>"""
    severity_counts: NotRequired[
        "aws_sdk_inspector2.types.severity_counts.SeverityCounts"
    ]
    """<p>The value to sort results by.</p>"""
    exploit_available_count: NotRequired["int"]
    """<p>The number of findings that have an exploit available.</p>"""
    fix_available_count: NotRequired["int"]
    """<p> Details about the number of fixes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingTypeAggregationResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import aws_sdk_inspector2.types.severity_counts

        out["severityCounts"] = aws_sdk_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "exploit_available_count" in value:
        out["exploitAvailableCount"] = value["exploit_available_count"]
    if "fix_available_count" in value:
        out["fixAvailableCount"] = value["fix_available_count"]
    return out


def deserialize_json(data: dict) -> FindingTypeAggregationResponse:
    out: FindingTypeAggregationResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import aws_sdk_inspector2.types.severity_counts

        out["severity_counts"] = (
            aws_sdk_inspector2.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    if "exploitAvailableCount" in data:
        out["exploit_available_count"] = data["exploitAvailableCount"]
    if "fixAvailableCount" in data:
        out["fix_available_count"] = data["fixAvailableCount"]
    return out
