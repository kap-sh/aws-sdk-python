"""Generated from Smithy shape ``com.amazonaws.directconnect#HasLogicalRedundancy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_direct_connect.errors import DeserializationError

HasLogicalRedundancy: TypeAlias = Literal[
    "unknown",
    "yes",
    "no",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknown",
        "yes",
        "no",
    )
)


def serialize_aws_json_1_1(value: HasLogicalRedundancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HasLogicalRedundancy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HasLogicalRedundancy value: {data!r}")
    return cast(HasLogicalRedundancy, data)
