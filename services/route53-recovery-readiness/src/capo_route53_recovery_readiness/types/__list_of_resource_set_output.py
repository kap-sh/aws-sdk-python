"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfResourceSetOutput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_readiness.types.resource_set_output

__listOfResourceSetOutput: TypeAlias = list[
    "capo_route53_recovery_readiness.types.resource_set_output.ResourceSetOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceSetOutput) -> list:
    import capo_route53_recovery_readiness.types.resource_set_output

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_readiness.types.resource_set_output.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfResourceSetOutput:
    import capo_route53_recovery_readiness.types.resource_set_output

    out: __listOfResourceSetOutput = []
    for item in data:
        out.append(
            capo_route53_recovery_readiness.types.resource_set_output.deserialize_json(
                item
            )
        )
    return out
