"""Generated from Smithy shape ``com.amazonaws.ssm#PatchOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchOperationType: TypeAlias = Literal[
    "Scan",
    "Install",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Scan",
        "Install",
    )
)


def serialize_aws_json_1_1(value: PatchOperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchOperationType value: {data!r}")
    return cast(PatchOperationType, data)
