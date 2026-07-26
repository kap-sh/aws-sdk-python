"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetCellReadinessSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.max_results


class GetCellReadinessSummaryRequest(TypedDict, closed=True):
    cell_name: "capo_route53_recovery_readiness.types.__string.__string"
    """<p>The name of the cell.</p>"""
    max_results: NotRequired[
        "capo_route53_recovery_readiness.types.max_results.MaxResults"
    ]
    """<p>The number of objects that you want to return with this call.</p>"""
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCellReadinessSummaryRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCellReadinessSummaryRequest:
    out: GetCellReadinessSummaryRequest = {}  # type: ignore[typeddict-item]
    return out
