"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfRecoveryGroupOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.recovery_group_output

__listOfRecoveryGroupOutput: TypeAlias = list[
    "capo_route53_recovery_readiness.types.recovery_group_output.RecoveryGroupOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfRecoveryGroupOutput) -> list:
    import capo_route53_recovery_readiness.types.recovery_group_output

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.recovery_group_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfRecoveryGroupOutput:
    import capo_route53_recovery_readiness.types.recovery_group_output

    out: __listOfRecoveryGroupOutput = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.recovery_group_output.deserialize_json(
                item
            )
        )
    return out
