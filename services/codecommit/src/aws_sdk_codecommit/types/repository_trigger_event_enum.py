"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerEventEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codecommit.errors import DeserializationError

RepositoryTriggerEventEnum: TypeAlias = Literal[
    "all",
    "updateReference",
    "createReference",
    "deleteReference",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "all",
        "updateReference",
        "createReference",
        "deleteReference",
    )
)


def serialize_aws_json_1_1(value: RepositoryTriggerEventEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryTriggerEventEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RepositoryTriggerEventEnum value: {data!r}"
        )
    return cast(RepositoryTriggerEventEnum, data)
