"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.resource

__listOfResource: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.resource.Resource"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfResource) -> list:
    import aws_sdk_route53_recovery_readiness.types.resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfResource:
    import aws_sdk_route53_recovery_readiness.types.resource

    out: __listOfResource = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.resource.deserialize_json(item)
        )
    return out
