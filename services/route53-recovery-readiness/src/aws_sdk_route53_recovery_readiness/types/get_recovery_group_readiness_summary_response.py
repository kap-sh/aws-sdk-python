"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetRecoveryGroupReadinessSummaryResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary
    import aws_sdk_route53_recovery_readiness.types.__string
    import aws_sdk_route53_recovery_readiness.types.readiness


class GetRecoveryGroupReadinessSummaryResponse(TypedDict):
    next_token: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__string.__string"
    ]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.readiness.Readiness"
    ]
    """<p>The readiness status at a recovery group level.</p>"""
    readiness_checks: NotRequired[
        "aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary.__listOfReadinessCheckSummary"
    ]
    """<p>Summaries of the readiness checks for the recovery group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecoveryGroupReadinessSummaryResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "readiness" in value:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.serialize_json(
                value["readiness"]
            )
        )
    if "readiness_checks" in value:
        import aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary

        out["readinessChecks"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary.serialize_json(
                value["readiness_checks"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecoveryGroupReadinessSummaryResponse:
    out: GetRecoveryGroupReadinessSummaryResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "readiness" in data:
        import aws_sdk_route53_recovery_readiness.types.readiness

        out["readiness"] = (
            aws_sdk_route53_recovery_readiness.types.readiness.deserialize_json(
                data["readiness"]
            )
        )
    if "readinessChecks" in data:
        import aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary

        out["readiness_checks"] = (
            aws_sdk_route53_recovery_readiness.types.__list_of_readiness_check_summary.deserialize_json(
                data["readinessChecks"]
            )
        )
    return out
