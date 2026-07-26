"""Generated from Smithy shape ``com.amazonaws.inspector2#AccountAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.severity_counts


class AccountAggregationResponse(TypedDict, closed=True):
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>The number of findings by severity.</p>"""
    exploit_available_count: NotRequired["int"]
    """<p> The number of findings that have an exploit available. </p>"""
    fix_available_count: NotRequired["int"]
    """<p> Details about the number of fixes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAggregationResponse) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "exploit_available_count" in value:
        out["exploitAvailableCount"] = value["exploit_available_count"]
    if "fix_available_count" in value:
        out["fixAvailableCount"] = value["fix_available_count"]
    return out


def deserialize_json(data: dict) -> AccountAggregationResponse:
    out: AccountAggregationResponse = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if "exploitAvailableCount" in data:
        out["exploit_available_count"] = data["exploitAvailableCount"]
    if "fixAvailableCount" in data:
        out["fix_available_count"] = data["fixAvailableCount"]
    return out
