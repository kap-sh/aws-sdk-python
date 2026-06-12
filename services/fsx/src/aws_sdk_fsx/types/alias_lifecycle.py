"""Generated from Smithy shape ``com.amazonaws.fsx#AliasLifecycle``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

AliasLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "CREATING",
        "DELETING",
        "CREATE_FAILED",
        "DELETE_FAILED",
    )
)


def serialize_aws_json_1_1(value: AliasLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AliasLifecycle:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AliasLifecycle value: {data!r}")
    return cast(AliasLifecycle, data)
