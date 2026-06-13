"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#DestinationCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_networkflowmonitor.errors import DeserializationError

DestinationCategory: TypeAlias = Literal[
    "INTRA_AZ",
    "INTER_AZ",
    "INTER_VPC",
    "UNCLASSIFIED",
    "AMAZON_S3",
    "AMAZON_DYNAMODB",
    "INTER_REGION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTRA_AZ",
        "INTER_AZ",
        "INTER_VPC",
        "UNCLASSIFIED",
        "AMAZON_S3",
        "AMAZON_DYNAMODB",
        "INTER_REGION",
    )
)


def serialize_json(value: DestinationCategory) -> str:
    return value


def deserialize_json(data: str) -> DestinationCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationCategory value: {data!r}")
    return cast(DestinationCategory, data)
