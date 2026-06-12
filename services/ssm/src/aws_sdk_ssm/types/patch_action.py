"""Generated from Smithy shape ``com.amazonaws.ssm#PatchAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchAction: TypeAlias = Literal[
    "ALLOW_AS_DEPENDENCY",
    "BLOCK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW_AS_DEPENDENCY",
        "BLOCK",
    )
)


def serialize_aws_json_1_1(value: PatchAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchAction value: {data!r}")
    return cast(PatchAction, data)
