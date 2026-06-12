"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsSubscriptionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_subscription_request

StandardsSubscriptionRequests: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_subscription_request.StandardsSubscriptionRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsSubscriptionRequests) -> list:
    import aws_sdk_securityhub.types.standards_subscription_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.standards_subscription_request.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsSubscriptionRequests:
    import aws_sdk_securityhub.types.standards_subscription_request

    out: StandardsSubscriptionRequests = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.standards_subscription_request.deserialize_json(
                item
            )
        )
    return out
