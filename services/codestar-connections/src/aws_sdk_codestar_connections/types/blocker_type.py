"""Generated from Smithy shape ``com.amazonaws.codestarconnections#BlockerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codestar_connections.errors import DeserializationError

BlockerType: TypeAlias = Literal["AUTOMATED",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("AUTOMATED",))


def serialize_aws_json_1_0(value: BlockerType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BlockerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BlockerType value: {data!r}")
    return cast(BlockerType, data)
