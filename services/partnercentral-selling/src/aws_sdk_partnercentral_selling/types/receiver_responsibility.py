"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ReceiverResponsibility``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

ReceiverResponsibility: TypeAlias = Literal[
    "Distributor",
    "Reseller",
    "Hardware Partner",
    "Managed Service Provider",
    "Software Partner",
    "Services Partner",
    "Training Partner",
    "Co-Sell Facilitator",
    "Facilitator",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Distributor",
        "Reseller",
        "Hardware Partner",
        "Managed Service Provider",
        "Software Partner",
        "Services Partner",
        "Training Partner",
        "Co-Sell Facilitator",
        "Facilitator",
    )
)


def serialize_aws_json_1_0(value: ReceiverResponsibility) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ReceiverResponsibility:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReceiverResponsibility value: {data!r}")
    return cast(ReceiverResponsibility, data)
