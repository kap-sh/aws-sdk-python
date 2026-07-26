"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineValueLabelRelativePosition``."""

from typing import Literal, TypeAlias, cast

ReferenceLineValueLabelRelativePosition: TypeAlias = Literal[
    "BEFORE_CUSTOM_LABEL",
    "AFTER_CUSTOM_LABEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineValueLabelRelativePosition) -> str:
    return value


def deserialize_json(data: str) -> ReferenceLineValueLabelRelativePosition:
    return cast(ReferenceLineValueLabelRelativePosition, data)
