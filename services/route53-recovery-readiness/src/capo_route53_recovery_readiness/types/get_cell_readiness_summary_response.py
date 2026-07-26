"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetCellReadinessSummaryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_readiness_check_summary
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.readiness


class GetCellReadinessSummaryResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness: NotRequired["capo_route53_recovery_readiness.types.readiness.Readiness"]
    """<p>The readiness at a cell level.</p>"""
    readiness_checks: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_readiness_check_summary.__listOfReadinessCheckSummary"
    ]
    """<p>Summaries for the readiness checks that make up the cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCellReadinessSummaryResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "readiness" in value:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "readiness_checks" in value:
        import capo_route53_recovery_readiness.types.__list_of_readiness_check_summary

        out["readinessChecks"] = (
            capo_route53_recovery_readiness.types.__list_of_readiness_check_summary.serialize_json(
                value["readiness_checks"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCellReadinessSummaryResponse:
    out: GetCellReadinessSummaryResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "readiness" in data:
        import capo_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            capo_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "readinessChecks" in data:
        import capo_route53_recovery_readiness.types.__list_of_readiness_check_summary

        out["readiness_checks"] = (
            capo_route53_recovery_readiness.types.__list_of_readiness_check_summary.deserialize_json(
                data["readinessChecks"]
            )
        )
    return out
