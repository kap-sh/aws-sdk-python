"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SortAsyncInvocationBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_runtime.errors import DeserializationError

SortAsyncInvocationBy: TypeAlias = Literal["SubmissionTime",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SubmissionTime",))


def serialize_json(value: SortAsyncInvocationBy) -> str:
    return value


def deserialize_json(data: str) -> SortAsyncInvocationBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortAsyncInvocationBy value: {data!r}")
    return cast(SortAsyncInvocationBy, data)
