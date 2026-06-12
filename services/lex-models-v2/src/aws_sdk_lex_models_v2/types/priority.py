"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#Priority``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

"""<p>The priority level of a recommendation.</p> <p>Valid values include:</p> <ul> <li> <p> <code>High</code> </p> </li> <li> <p> <code>Medium</code> </p> </li> <li> <p> <code>Low</code> </p> </li> </ul>"""
Priority: TypeAlias = Literal[
    "High",
    "Medium",
    "Low",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "High",
        "Medium",
        "Low",
    )
)


def serialize_json(value: Priority) -> str:
    return value


def deserialize_json(data: str) -> Priority:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Priority value: {data!r}")
    return cast(Priority, data)
