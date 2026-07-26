"""Generated from Smithy shape ``com.amazonaws.vpclattice#AccessLogSubscriptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.access_log_subscription_summary

AccessLogSubscriptionList: TypeAlias = list[
    "capo_vpc_lattice.types.access_log_subscription_summary.AccessLogSubscriptionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessLogSubscriptionList) -> list:
    import capo_vpc_lattice.types.access_log_subscription_summary

    out: list = []
    for item in value:
        out.append(
            capo_vpc_lattice.types.access_log_subscription_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessLogSubscriptionList:
    import capo_vpc_lattice.types.access_log_subscription_summary

    out: AccessLogSubscriptionList = []
    for item in data:
        out.append(
            capo_vpc_lattice.types.access_log_subscription_summary.deserialize_json(
                item
            )
        )
    return out
