"""Generated from Smithy shape ``com.amazonaws.securityhub#Partition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

Partition: TypeAlias = Literal[
    "aws",
    "aws-cn",
    "aws-us-gov",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "aws",
        "aws-cn",
        "aws-us-gov",
    )
)


def serialize_json(value: Partition) -> str:
    return value


def deserialize_json(data: str) -> Partition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Partition value: {data!r}")
    return cast(Partition, data)
