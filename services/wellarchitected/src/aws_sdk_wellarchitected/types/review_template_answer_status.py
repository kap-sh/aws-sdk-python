"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ReviewTemplateAnswerStatus``."""

from typing import Literal, TypeAlias, cast

ReviewTemplateAnswerStatus: TypeAlias = Literal[
    "UNANSWERED",
    "ANSWERED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReviewTemplateAnswerStatus) -> str:
    return value


def deserialize_json(data: str) -> ReviewTemplateAnswerStatus:
    return cast(ReviewTemplateAnswerStatus, data)
