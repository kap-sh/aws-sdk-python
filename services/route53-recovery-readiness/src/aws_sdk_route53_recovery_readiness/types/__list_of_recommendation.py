"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfRecommendation``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.recommendation

__listOfRecommendation: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.recommendation.Recommendation"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRecommendation) -> list:
    import aws_sdk_route53_recovery_readiness.types.recommendation

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.recommendation.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfRecommendation:
    import aws_sdk_route53_recovery_readiness.types.recommendation

    out: __listOfRecommendation = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.recommendation.deserialize_json(
                item
            )
        )
    return out
