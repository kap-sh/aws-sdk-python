"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscription

StandardsSubscriptions: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_subscription.StandardsSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscriptions) -> list:
    import aws_sdk_securityhub.types.standards_subscription

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.standards_subscription.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StandardsSubscriptions:
    import aws_sdk_securityhub.types.standards_subscription

    out: StandardsSubscriptions = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.standards_subscription.deserialize_json(item)
        )
    return out
