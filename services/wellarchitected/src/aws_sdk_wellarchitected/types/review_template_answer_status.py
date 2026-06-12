"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateAnswerStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wellarchitected.errors import DeserializationError

ReviewTemplateAnswerStatus: TypeAlias = Literal[
    "UNANSWERED",
    "ANSWERED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNANSWERED",
        "ANSWERED",
    )
)


def serialize_json(value: ReviewTemplateAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewTemplateAnswerStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ReviewTemplateAnswerStatus value: {data!r}"
        )
    return cast(ReviewTemplateAnswerStatus, data)
