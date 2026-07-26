"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#ListReadinessChecksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_readiness_check_output
    import capo_route53_recovery_readiness.types.__string


class ListReadinessChecksResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    readiness_checks: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_readiness_check_output.__listOfReadinessCheckOutput"
    ]
    """<p>A list of readiness checks associated with the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReadinessChecksResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "readiness_checks" in value:
        import capo_route53_recovery_readiness.types.__list_of_readiness_check_output

        out["readinessChecks"] = (
            capo_route53_recovery_readiness.types.__list_of_readiness_check_output.serialize_json(
                value["readiness_checks"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReadinessChecksResponse:
    out: ListReadinessChecksResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "readinessChecks" in data:
        import capo_route53_recovery_readiness.types.__list_of_readiness_check_output

        out["readiness_checks"] = (
            capo_route53_recovery_readiness.types.__list_of_readiness_check_output.deserialize_json(
                data["readinessChecks"]
            )
        )
    return out
