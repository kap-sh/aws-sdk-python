"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictResolutionStrategyTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

ConflictResolutionStrategyTypeEnum: TypeAlias = Literal[
    "NONE",
    "ACCEPT_SOURCE",
    "ACCEPT_DESTINATION",
    "AUTOMERGE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "ACCEPT_SOURCE",
        "ACCEPT_DESTINATION",
        "AUTOMERGE",
    )
)


def serialize_aws_json_1_1(value: ConflictResolutionStrategyTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictResolutionStrategyTypeEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConflictResolutionStrategyTypeEnum value: {data!r}"
        )
    return cast(ConflictResolutionStrategyTypeEnum, data)
