"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceIndexRotationPeriod``."""

from typing import Literal, TypeAlias, cast

AmazonopensearchserviceIndexRotationPeriod: TypeAlias = Literal[
    "NoRotation",
    "OneHour",
    "OneDay",
    "OneWeek",
    "OneMonth",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonopensearchserviceIndexRotationPeriod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonopensearchserviceIndexRotationPeriod:
    return cast(AmazonopensearchserviceIndexRotationPeriod, data)
