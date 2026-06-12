"""Generated from Smithy shape ``com.amazonaws.ssm#RebootOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

RebootOption: TypeAlias = Literal[
    "RebootIfNeeded",
    "NoReboot",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RebootIfNeeded",
        "NoReboot",
    )
)


def serialize_aws_json_1_1(value: RebootOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RebootOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RebootOption value: {data!r}")
    return cast(RebootOption, data)
