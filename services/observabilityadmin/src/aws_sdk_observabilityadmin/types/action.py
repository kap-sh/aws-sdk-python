"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#Action``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: Action) -> str:
    return value


def deserialize_json(data: str) -> Action:
    return cast(Action, data)
