"""Generated from Smithy shape ``com.amazonaws.route53recoveryreadiness#Readiness``."""

from typing import Literal, TypeAlias, cast

"""<p>The readiness status.</p>"""
Readiness: TypeAlias = Literal[
    "READY",
    "NOT_READY",
    "UNKNOWN",
    "NOT_AUTHORIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Readiness) -> str:
    return value


def deserialize_json(data: str) -> Readiness:
    return cast(Readiness, data)
