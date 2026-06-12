"""Generated from Smithy shape ``com.amazonaws.fsx#OpenZFSCopyStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

OpenZFSCopyStrategy: TypeAlias = Literal[
    "CLONE",
    "FULL_COPY",
    "INCREMENTAL_COPY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLONE",
        "FULL_COPY",
        "INCREMENTAL_COPY",
    )
)


def serialize_aws_json_1_1(value: OpenZFSCopyStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OpenZFSCopyStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenZFSCopyStrategy value: {data!r}")
    return cast(OpenZFSCopyStrategy, data)
