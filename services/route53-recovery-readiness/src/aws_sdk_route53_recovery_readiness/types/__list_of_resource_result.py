"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfResourceResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.resource_result

__listOfResourceResult: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.resource_result.ResourceResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResourceResult) -> list:
    import aws_sdk_route53_recovery_readiness.types.resource_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.resource_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfResourceResult:
    import aws_sdk_route53_recovery_readiness.types.resource_result

    out: __listOfResourceResult = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.resource_result.deserialize_json(
                item
            )
        )
    return out
