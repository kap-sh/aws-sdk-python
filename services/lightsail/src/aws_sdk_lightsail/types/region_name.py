"""Generated from Smithy shape ``com.amazonaws.lightsail#RegionName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

RegionName: TypeAlias = Literal[
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-central-1",
    "eu-north-1",
    "eu-south-2",
    "ca-central-1",
    "ap-east-1",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-southeast-3",
    "ap-southeast-5",
    "sa-east-1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "eu-central-1",
        "eu-north-1",
        "eu-south-2",
        "ca-central-1",
        "ap-east-1",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-southeast-3",
        "ap-southeast-5",
        "sa-east-1",
    )
)


def serialize_aws_json_1_1(value: RegionName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegionName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionName value: {data!r}")
    return cast(RegionName, data)
