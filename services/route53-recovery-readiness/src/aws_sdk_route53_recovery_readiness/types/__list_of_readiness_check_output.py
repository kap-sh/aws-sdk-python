"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfReadinessCheckOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_output

__listOfReadinessCheckOutput: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.readiness_check_output.ReadinessCheckOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfReadinessCheckOutput) -> list:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.readiness_check_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfReadinessCheckOutput:
    import aws_sdk_route53_recovery_readiness.types.readiness_check_output

    out: __listOfReadinessCheckOutput = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.readiness_check_output.deserialize_json(
                item
            )
        )
    return out
