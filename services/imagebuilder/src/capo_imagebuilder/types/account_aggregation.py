"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AccountAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.severity_counts


class AccountAggregation(TypedDict, closed=True):
    account_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Identifies the account that owns the aggregated resource findings.</p>"""
    severity_counts: NotRequired[
        "capo_imagebuilder.types.severity_counts.SeverityCounts"
    ]
    """<p>Counts by severity level for medium severity and higher level findings, plus a total for all of the findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountAggregation) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_imagebuilder.types.severity_counts

        out["severityCounts"] = capo_imagebuilder.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> AccountAggregation:
    out: AccountAggregation = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "severityCounts" in data:
        import capo_imagebuilder.types.severity_counts

        out["severity_counts"] = (
            capo_imagebuilder.types.severity_counts.deserialize_json(
                data["severityCounts"]
            )
        )
    return out
