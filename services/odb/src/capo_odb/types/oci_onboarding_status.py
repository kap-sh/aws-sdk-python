"""Generated from Smithy shape ``com.amazonaws.odb#OciOnboardingStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: OciOnboardingStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OciOnboardingStatus:
    return cast(OciOnboardingStatus, data)
