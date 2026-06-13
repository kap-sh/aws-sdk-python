"""Generated from Smithy shape ``com.amazonaws.odb#IormLifecycleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

IormLifecycleState: TypeAlias = Literal[
    "BOOTSTRAPPING",
    "DISABLED",
    "ENABLED",
    "FAILED",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOOTSTRAPPING",
        "DISABLED",
        "ENABLED",
        "FAILED",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: IormLifecycleState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IormLifecycleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IormLifecycleState value: {data!r}")
    return cast(IormLifecycleState, data)
