"""Generated from Smithy shape ``com.amazonaws.sesv2#DeliverabilityDashboardAccountStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sesv2.errors import DeserializationError

"""<p>The current status of your Deliverability dashboard subscription. If this value is <code>PENDING_EXPIRATION</code>, your subscription is scheduled to expire at the end of the current calendar month.</p>"""
DeliverabilityDashboardAccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "PENDING_EXPIRATION",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PENDING_EXPIRATION",
        "DISABLED",
    )
)


def serialize_json(value: DeliverabilityDashboardAccountStatus) -> str:
    return value


def deserialize_json(data: str) -> DeliverabilityDashboardAccountStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DeliverabilityDashboardAccountStatus value: {data!r}"
        )
    return cast(DeliverabilityDashboardAccountStatus, data)
