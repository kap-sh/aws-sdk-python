"""Generated from Smithy shape ``com.amazonaws.odb#OciOnboardingStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

"""<p/>"""
OciOnboardingStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "PENDING_LINK_GENERATION",
    "PENDING_CUSTOMER_ACTION",
    "PENDING_INITIALIZATION",
    "ACTIVATING",
    "ACTIVE_IN_HOME_REGION",
    "ACTIVE",
    "ACTIVE_LIMITED",
    "FAILED",
    "PUBLIC_OFFER_UNSUPPORTED",
    "SUSPENDED",
    "CANCELED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_STARTED",
        "PENDING_LINK_GENERATION",
        "PENDING_CUSTOMER_ACTION",
        "PENDING_INITIALIZATION",
        "ACTIVATING",
        "ACTIVE_IN_HOME_REGION",
        "ACTIVE",
        "ACTIVE_LIMITED",
        "FAILED",
        "PUBLIC_OFFER_UNSUPPORTED",
        "SUSPENDED",
        "CANCELED",
    )
)


def serialize_aws_json_1_0(value: OciOnboardingStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OciOnboardingStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OciOnboardingStatus value: {data!r}")
    return cast(OciOnboardingStatus, data)
