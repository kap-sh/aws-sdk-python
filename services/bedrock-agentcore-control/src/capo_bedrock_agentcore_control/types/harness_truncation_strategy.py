"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessTruncationStrategy``."""

from typing import Literal, TypeAlias, cast

HarnessTruncationStrategy: TypeAlias = Literal[
    "sliding_window",
    "summarization",
    "none",
]


# --- restJson1 ser/de ---
def serialize_json(value: HarnessTruncationStrategy) -> str:
    return value


def deserialize_json(data: str) -> HarnessTruncationStrategy:
    return cast(HarnessTruncationStrategy, data)
