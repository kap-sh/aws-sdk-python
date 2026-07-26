"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_subscription

StandardsSubscriptions: TypeAlias = list[
    "capo_securityhub.types.standards_subscription.StandardsSubscription"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscriptions) -> list:
    import capo_securityhub.types.standards_subscription

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.standards_subscription.serialize_json(item))
    return out


def deserialize_json(data: list) -> StandardsSubscriptions:
    import capo_securityhub.types.standards_subscription

    out: StandardsSubscriptions = []
    for item in data:
        out.append(capo_securityhub.types.standards_subscription.deserialize_json(item))
    return out
