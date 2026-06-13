"""Generated from Smithy shape ``com.amazonaws.quicksight#ConditionalFormattingIconDisplayOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

ConditionalFormattingIconDisplayOption: TypeAlias = Literal["ICON_ONLY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ICON_ONLY",))


def serialize_json(value: ConditionalFormattingIconDisplayOption) -> str:
    return value


def deserialize_json(data: str) -> ConditionalFormattingIconDisplayOption:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConditionalFormattingIconDisplayOption value: {data!r}"
        )
    return cast(ConditionalFormattingIconDisplayOption, data)
