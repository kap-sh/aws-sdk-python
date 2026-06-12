"""Generated from Smithy shape ``com.amazonaws.sfn#KmsKeyState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sfn.errors import DeserializationError

KmsKeyState: TypeAlias = Literal[
    "DISABLED",
    "PENDING_DELETION",
    "PENDING_IMPORT",
    "UNAVAILABLE",
    "CREATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "PENDING_DELETION",
        "PENDING_IMPORT",
        "UNAVAILABLE",
        "CREATING",
    )
)


def serialize_aws_json_1_0(value: KmsKeyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KmsKeyState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KmsKeyState value: {data!r}")
    return cast(KmsKeyState, data)
