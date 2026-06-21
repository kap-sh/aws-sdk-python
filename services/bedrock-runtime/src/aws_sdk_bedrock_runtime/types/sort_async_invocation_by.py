"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SortAsyncInvocationBy``."""

from typing import Literal, TypeAlias, cast

SortAsyncInvocationBy: TypeAlias = Literal["SubmissionTime",]


# --- restJson1 ser/de ---
def serialize_json(value: SortAsyncInvocationBy) -> str:
    return value


def deserialize_json(data: str) -> SortAsyncInvocationBy:
    return cast(SortAsyncInvocationBy, data)
