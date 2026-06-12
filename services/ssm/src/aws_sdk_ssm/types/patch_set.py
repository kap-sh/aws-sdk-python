"""Generated from Smithy shape ``com.amazonaws.ssm#PatchSet``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchSet: TypeAlias = Literal[
    "OS",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OS",
        "APPLICATION",
    )
)


def serialize_aws_json_1_1(value: PatchSet) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchSet:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchSet value: {data!r}")
    return cast(PatchSet, data)
