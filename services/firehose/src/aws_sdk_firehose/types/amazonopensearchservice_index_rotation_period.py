"""Generated from Smithy shape ``com.amazonaws.firehose#AmazonopensearchserviceIndexRotationPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

AmazonopensearchserviceIndexRotationPeriod: TypeAlias = Literal[
    "NoRotation",
    "OneHour",
    "OneDay",
    "OneWeek",
    "OneMonth",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NoRotation",
        "OneHour",
        "OneDay",
        "OneWeek",
        "OneMonth",
    )
)


def serialize_aws_json_1_1(value: AmazonopensearchserviceIndexRotationPeriod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AmazonopensearchserviceIndexRotationPeriod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AmazonopensearchserviceIndexRotationPeriod value: {data!r}"
        )
    return cast(AmazonopensearchserviceIndexRotationPeriod, data)
