"""Generated from Smithy shape ``com.amazonaws.cleanrooms#SupportedS3Region``."""

from typing import Literal, TypeAlias, cast

SupportedS3Region: TypeAlias = Literal[
    "us-west-1",
    "us-west-2",
    "us-east-1",
    "us-east-2",
    "af-south-1",
    "ap-east-1",
    "ap-east-2",
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
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedS3Region) -> str:
    return value


def deserialize_json(data: str) -> SupportedS3Region:
    return cast(SupportedS3Region, data)
