"""Generated from Smithy shape ``com.amazonaws.quicksight#TopicFilterOperator``."""

from typing import Literal, TypeAlias, cast

TopicFilterOperator: TypeAlias = Literal[
    "StringEquals",
    "StringLike",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicFilterOperator) -> str:
    return value


def deserialize_json(data: str) -> TopicFilterOperator:
    return cast(TopicFilterOperator, data)
