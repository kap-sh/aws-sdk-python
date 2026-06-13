"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormButtonsPosition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

FormButtonsPosition: TypeAlias = Literal[
    "top",
    "bottom",
    "top_and_bottom",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "top",
        "bottom",
        "top_and_bottom",
    )
)


def serialize_json(value: FormButtonsPosition) -> str:
    return value


def deserialize_json(data: str) -> FormButtonsPosition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormButtonsPosition value: {data!r}")
    return cast(FormButtonsPosition, data)
