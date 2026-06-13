"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddonSubscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_subscription

AddonSubscriptions: TypeAlias = list[
    "aws_sdk_mailmanager.types.addon_subscription.AddonSubscription"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddonSubscriptions) -> list:
    import aws_sdk_mailmanager.types.addon_subscription

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.addon_subscription.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AddonSubscriptions:
    import aws_sdk_mailmanager.types.addon_subscription

    out: AddonSubscriptions = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.addon_subscription.deserialize_aws_json_1_0(item)
        )
    return out
