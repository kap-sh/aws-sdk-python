"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconDisplayOption``."""

from typing import Literal, TypeAlias, cast

ConditionalFormattingIconDisplayOption: TypeAlias = Literal["ICON_ONLY",]


# --- restJson1 ser/de ---
def serialize_json(value: ConditionalFormattingIconDisplayOption) -> str:
    return value


def deserialize_json(data: str) -> ConditionalFormattingIconDisplayOption:
    return cast(ConditionalFormattingIconDisplayOption, data)
