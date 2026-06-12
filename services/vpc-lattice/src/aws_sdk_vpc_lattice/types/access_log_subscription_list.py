"""Generated from Smithy shape ``com.amazonaws.vpclattice#AccessLogSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.access_log_subscription_summary

AccessLogSubscriptionList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.access_log_subscription_summary.AccessLogSubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessLogSubscriptionList) -> list:
    import aws_sdk_vpc_lattice.types.access_log_subscription_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_vpc_lattice.types.access_log_subscription_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AccessLogSubscriptionList:
    import aws_sdk_vpc_lattice.types.access_log_subscription_summary

    out: AccessLogSubscriptionList = []
    for item in data:
        out.append(
            aws_sdk_vpc_lattice.types.access_log_subscription_summary.deserialize_json(
                item
            )
        )
    return out
