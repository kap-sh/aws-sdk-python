"""Generated from Smithy shape ``com.amazonaws.neptunedata#S3BucketRegion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptunedata.errors import DeserializationError

S3BucketRegion: TypeAlias = Literal[
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "ca-central-1",
    "sa-east-1",
    "eu-north-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-central-1",
    "me-south-1",
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-south-1",
    "cn-north-1",
    "cn-northwest-1",
    "us-gov-west-1",
    "us-gov-east-1",
    "ca-west-1",
    "eu-south-2",
    "il-central-1",
    "me-central-1",
    "ap-northeast-3",
    "ap-southeast-3",
    "ap-southeast-4",
    "ap-southeast-5",
    "ap-southeast-7",
    "mx-central-1",
    "ap-east-2",
    "ap-south-2",
    "eu-central-2",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "ca-central-1",
        "sa-east-1",
        "eu-north-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "eu-central-1",
        "me-south-1",
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-south-1",
        "cn-north-1",
        "cn-northwest-1",
        "us-gov-west-1",
        "us-gov-east-1",
        "ca-west-1",
        "eu-south-2",
        "il-central-1",
        "me-central-1",
        "ap-northeast-3",
        "ap-southeast-3",
        "ap-southeast-4",
        "ap-southeast-5",
        "ap-southeast-7",
        "mx-central-1",
        "ap-east-2",
        "ap-south-2",
        "eu-central-2",
    )
)


def serialize_json(value: S3BucketRegion) -> str:
    return value


def deserialize_json(data: str) -> S3BucketRegion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown S3BucketRegion value: {data!r}")
    return cast(S3BucketRegion, data)
