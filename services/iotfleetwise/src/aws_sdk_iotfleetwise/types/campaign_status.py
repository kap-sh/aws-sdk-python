"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CampaignStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

CampaignStatus: TypeAlias = Literal[
    "CREATING",
    "WAITING_FOR_APPROVAL",
    "RUNNING",
    "SUSPENDED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "WAITING_FOR_APPROVAL",
        "RUNNING",
        "SUSPENDED",
    )
)


def serialize_aws_json_1_0(value: CampaignStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CampaignStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CampaignStatus value: {data!r}")
    return cast(CampaignStatus, data)
