"""Generated from Smithy shape ``com.amazonaws.greengrass#__listOfSubscription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.subscription

__listOfSubscription: TypeAlias = list[
    "aws_sdk_greengrass.types.subscription.Subscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfSubscription) -> list:
    import aws_sdk_greengrass.types.subscription

    out: list = []
    for item in value:
        out.append(aws_sdk_greengrass.types.subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfSubscription:
    import aws_sdk_greengrass.types.subscription

    out: __listOfSubscription = []
    for item in data:
        out.append(aws_sdk_greengrass.types.subscription.deserialize_json(item))
    return out
