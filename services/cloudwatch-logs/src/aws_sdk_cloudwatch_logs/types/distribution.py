"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Distribution``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch_logs.errors import DeserializationError

"""<p>The method used to distribute log data to the destination, which can be either random or grouped by log stream.</p>"""
Distribution: TypeAlias = Literal[
    "Random",
    "ByLogStream",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Random",
        "ByLogStream",
    )
)


def serialize_aws_json_1_1(value: Distribution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Distribution:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Distribution value: {data!r}")
    return cast(Distribution, data)
