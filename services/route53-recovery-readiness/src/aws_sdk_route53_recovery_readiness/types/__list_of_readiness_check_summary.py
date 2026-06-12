"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfReadinessCheckSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_summary

__listOfReadinessCheckSummary: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.readiness_check_summary.ReadinessCheckSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReadinessCheckSummary) -> list:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.readiness_check_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfReadinessCheckSummary:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_summary

    out: __listOfReadinessCheckSummary = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.readiness_check_summary.deserialize_json(
                item
            )
        )
    return out
