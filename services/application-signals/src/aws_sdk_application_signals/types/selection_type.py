"""Generated from Smithy shape ``com.amazonaws.applicationsignals#SelectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

"""<p>The strategy for selecting operations to include in a service-level SLO.</p> <ul> <li> <p> <code>EXPLICIT</code> — You provide a specific list of operations in the <code>Components</code> field of <code>CompositeSliConfig</code>.</p> </li> <li> <p> <code>PREFIX</code> — You provide a prefix string in the <code>Pattern</code> field of <code>SelectionConfig</code>, and all operations whose names start with the prefix are included.</p> </li> <li> <p> <code>REGEX</code> — You provide a regular expression in the <code>Pattern</code> field of <code>SelectionConfig</code>, and all operations whose names match the pattern are included.</p> </li> </ul>"""
SelectionType: TypeAlias = Literal[
    "EXPLICIT",
    "PREFIX",
    "REGEX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXPLICIT",
        "PREFIX",
        "REGEX",
    )
)


def serialize_json(value: SelectionType) -> str:
    return value


def deserialize_json(data: str) -> SelectionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectionType value: {data!r}")
    return cast(SelectionType, data)
