"""Generated from Smithy shape ``com.amazonaws.fms#MarketplaceSubscriptionOnboardingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

MarketplaceSubscriptionOnboardingStatus: TypeAlias = Literal[
    "NO_SUBSCRIPTION",
    "NOT_COMPLETE",
    "COMPLETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_SUBSCRIPTION",
        "NOT_COMPLETE",
        "COMPLETE",
    )
)


def serialize_aws_json_1_1(value: MarketplaceSubscriptionOnboardingStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MarketplaceSubscriptionOnboardingStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MarketplaceSubscriptionOnboardingStatus value: {data!r}"
        )
    return cast(MarketplaceSubscriptionOnboardingStatus, data)
