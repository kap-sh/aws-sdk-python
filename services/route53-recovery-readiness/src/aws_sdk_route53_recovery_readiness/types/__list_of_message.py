"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#__listOfMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_readiness.types.message

__listOfMessage: TypeAlias = list[
    "aws_sdk_route53_recovery_readiness.types.message.Message"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMessage) -> list:
    import aws_sdk_route53_recovery_readiness.types.message

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_readiness.types.message.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfMessage:
    import aws_sdk_route53_recovery_readiness.types.message

    out: __listOfMessage = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_readiness.types.message.deserialize_json(item)
        )
    return out
