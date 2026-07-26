"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#GetArchitectureRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.__list_of_recommendation
    import capo_route53_recovery_readiness.types.__string
    import capo_route53_recovery_readiness.types.last_audit_timestamp


class GetArchitectureRecommendationsResponse(TypedDict, closed=True):
    last_audit_timestamp: NotRequired[
        "capo_route53_recovery_readiness.types.last_audit_timestamp.LastAuditTimestamp"
    ]
    """<p>The time that a recovery group was last assessed for recommendations, in UTC ISO-8601 format.</p>"""
    next_token: NotRequired["capo_route53_recovery_readiness.types.__string.__string"]
    """<p>The token that identifies which batch of results you want to see.</p>"""
    recommendations: NotRequired[
        "capo_route53_recovery_readiness.types.__list_of_recommendation.__listOfRecommendation"
    ]
    """<p>A list of the recommendations for the customer's application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetArchitectureRecommendationsResponse) -> dict:
    out: dict = {}
    if "last_audit_timestamp" in value:
        import capo_route53_recovery_readiness.types.last_audit_timestamp

        out["lastAuditTimestamp"] = (
            capo_route53_recovery_readiness.types.last_audit_timestamp.serialize_json(
                value["last_audit_timestamp"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "recommendations" in value:
        import capo_route53_recovery_readiness.types.__list_of_recommendation

        out["recommendations"] = (
            capo_route53_recovery_readiness.types.__list_of_recommendation.serialize_json(
                value["recommendations"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetArchitectureRecommendationsResponse:
    out: GetArchitectureRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "lastAuditTimestamp" in data:
        import capo_route53_recovery_readiness.types.last_audit_timestamp

        out["last_audit_timestamp"] = (
            capo_route53_recovery_readiness.types.last_audit_timestamp.deserialize_json(
                data["lastAuditTimestamp"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "recommendations" in data:
        import capo_route53_recovery_readiness.types.__list_of_recommendation

        out["recommendations"] = (
            capo_route53_recovery_readiness.types.__list_of_recommendation.deserialize_json(
                data["recommendations"]
            )
        )
    return out
