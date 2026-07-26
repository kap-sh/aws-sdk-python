"""Generated from Smithy shape ``com.amazonaws.pinpointemail#DeliverabilityDashboardAccountStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The current status of your Deliverability dashboard subscription. If this value is <code>PENDING_EXPIRATION</code>, your subscription is scheduled to expire at the end of the current calendar month.</p>"""
DeliverabilityDashboardAccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_EXPIRATION",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliverabilityDashboardAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliverabilityDashboardAccountStatus:
    return cast(DeliverabilityDashboardAccountStatus, data)
