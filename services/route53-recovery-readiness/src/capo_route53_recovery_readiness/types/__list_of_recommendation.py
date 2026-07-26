"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfRecommendation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.recommendation

__listOfRecommendation: TypeAlias = list[
    "capo_route53_recovery_readiness.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRecommendation) -> list:
    import capo_route53_recovery_readiness.types.recommendation

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfRecommendation:
    import capo_route53_recovery_readiness.types.recommendation

    out: __listOfRecommendation = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.recommendation.deserialize_json(item)
        )
    return out
