"""Generated from Smithy shape ``com.amazonaws.datazone#SubscriptionRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.subscription_request_summary

SubscriptionRequests: TypeAlias = list[
    "aws_sdk_datazone.types.subscription_request_summary.SubscriptionRequestSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionRequests) -> list:
    import aws_sdk_datazone.types.subscription_request_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_datazone.types.subscription_request_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubscriptionRequests:
    import aws_sdk_datazone.types.subscription_request_summary

    out: SubscriptionRequests = []
    for item in data:
        out.append(
            aws_sdk_datazone.types.subscription_request_summary.deserialize_json(item)
        )
    return out
