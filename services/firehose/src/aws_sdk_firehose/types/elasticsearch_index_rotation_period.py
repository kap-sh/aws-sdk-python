"""Generated from Smithy shape ``com.amazonaws.firehose#ElasticsearchIndexRotationPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

ElasticsearchIndexRotationPeriod: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ElasticsearchIndexRotationPeriod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ElasticsearchIndexRotationPeriod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ElasticsearchIndexRotationPeriod value: {data!r}"
        )
    return cast(ElasticsearchIndexRotationPeriod, data)
