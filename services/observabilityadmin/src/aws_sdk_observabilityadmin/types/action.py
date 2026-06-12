"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Action``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

"""<p> Enumeration of WAF actions that can be matched in filter conditions. </p>"""
Action: TypeAlias = Literal[
    "ALLOW",
    "BLOCK",
    "COUNT",
    "CAPTCHA",
    "CHALLENGE",
    "EXCLUDED_AS_COUNT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "BLOCK",
        "COUNT",
        "CAPTCHA",
        "CHALLENGE",
        "EXCLUDED_AS_COUNT",
    )
)


def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Action value: {data!r}")
    return cast(Action, data)
