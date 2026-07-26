"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentCriteriaOperator``."""

from typing import Literal, TypeAlias, cast

CustomActionAttachmentCriteriaOperator: TypeAlias = Literal[
    "HAS_VALUE",
    "EQUALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachmentCriteriaOperator) -> str:
    return value


def deserialize_json(data: str) -> CustomActionAttachmentCriteriaOperator:
    return cast(CustomActionAttachmentCriteriaOperator, data)
