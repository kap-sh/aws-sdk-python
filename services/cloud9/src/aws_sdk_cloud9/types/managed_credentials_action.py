"""Generated from Smithy shape ``com.amazonaws.cloud9#ManagedCredentialsAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloud9.errors import DeserializationError

ManagedCredentialsAction: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_aws_json_1_1(value: ManagedCredentialsAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedCredentialsAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedCredentialsAction value: {data!r}")
    return cast(ManagedCredentialsAction, data)
