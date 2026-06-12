"""Generated from Smithy shape ``com.amazonaws.macie2#FindingsFilterAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The action to perform on findings that match the filter criteria. To suppress (automatically archive) findings that match the criteria, set this value to ARCHIVE. Valid values are:</p>"""
FindingsFilterAction: TypeAlias = Literal[
    "ARCHIVE",
    "NOOP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARCHIVE",
        "NOOP",
    )
)


def serialize_json(value: FindingsFilterAction) -> str:
    return value


def deserialize_json(data: str) -> FindingsFilterAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FindingsFilterAction value: {data!r}")
    return cast(FindingsFilterAction, data)
