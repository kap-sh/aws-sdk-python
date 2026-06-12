"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateCampaignAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

UpdateCampaignAction: TypeAlias = Literal[
    "APPROVE",
    "SUSPEND",
    "RESUME",
    "UPDATE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPROVE",
        "SUSPEND",
        "RESUME",
        "UPDATE",
    )
)


def serialize_aws_json_1_0(value: UpdateCampaignAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> UpdateCampaignAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateCampaignAction value: {data!r}")
    return cast(UpdateCampaignAction, data)
