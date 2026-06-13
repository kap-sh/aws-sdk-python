"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CommercialRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

CommercialRegion: TypeAlias = Literal[
    "us-west-1",
    "us-west-2",
    "us-east-1",
    "us-east-2",
    "af-south-1",
    "ap-east-1",
    "ap-south-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-southeast-3",
    "ap-southeast-5",
    "ap-southeast-4",
    "ap-southeast-7",
    "ap-south-1",
    "ap-northeast-3",
    "ap-northeast-1",
    "ap-northeast-2",
    "ca-central-1",
    "ca-west-1",
    "eu-south-1",
    "eu-west-3",
    "eu-south-2",
    "eu-central-2",
    "eu-central-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "me-south-1",
    "me-central-1",
    "il-central-1",
    "sa-east-1",
    "mx-central-1",
    "ap-east-2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-west-1",
        "us-west-2",
        "us-east-1",
        "us-east-2",
        "af-south-1",
        "ap-east-1",
        "ap-south-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-southeast-5",
        "ap-southeast-4",
        "ap-southeast-7",
        "ap-south-1",
        "ap-northeast-3",
        "ap-northeast-1",
        "ap-northeast-2",
        "ca-central-1",
        "ca-west-1",
        "eu-south-1",
        "eu-west-3",
        "eu-south-2",
        "eu-central-2",
        "eu-central-1",
        "eu-north-1",
        "eu-west-1",
        "eu-west-2",
        "me-south-1",
        "me-central-1",
        "il-central-1",
        "sa-east-1",
        "mx-central-1",
        "ap-east-2",
    )
)


def serialize_json(value: CommercialRegion) -> str:
    return value


def deserialize_json(data: str) -> CommercialRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CommercialRegion value: {data!r}")
    return cast(CommercialRegion, data)
