"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentCriteriaOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chatbot.errors import DeserializationError

CustomActionAttachmentCriteriaOperator: TypeAlias = Literal[
    "HAS_VALUE",
    "EQUALS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HAS_VALUE",
        "EQUALS",
    )
)


def serialize_json(value: CustomActionAttachmentCriteriaOperator) -> str:
    return value


def deserialize_json(data: str) -> CustomActionAttachmentCriteriaOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomActionAttachmentCriteriaOperator value: {data!r}"
        )
    return cast(CustomActionAttachmentCriteriaOperator, data)
