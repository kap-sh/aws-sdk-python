"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ColorTheme``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_web.errors import DeserializationError

ColorTheme: TypeAlias = Literal[
    "Light",
    "Dark",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Light",
        "Dark",
    )
)


def serialize_json(value: ColorTheme) -> str:
    return value


def deserialize_json(data: str) -> ColorTheme:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorTheme value: {data!r}")
    return cast(ColorTheme, data)
