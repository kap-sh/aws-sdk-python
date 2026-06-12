"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeOptionTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

MergeOptionTypeEnum: TypeAlias = Literal[
    "FAST_FORWARD_MERGE",
    "SQUASH_MERGE",
    "THREE_WAY_MERGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FAST_FORWARD_MERGE",
        "SQUASH_MERGE",
        "THREE_WAY_MERGE",
    )
)


def serialize_aws_json_1_1(value: MergeOptionTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MergeOptionTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MergeOptionTypeEnum value: {data!r}")
    return cast(MergeOptionTypeEnum, data)
