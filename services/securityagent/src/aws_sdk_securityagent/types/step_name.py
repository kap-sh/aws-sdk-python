"""Generated from Smithy shape ``com.amazonaws.securityagent#StepName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityagent.errors import DeserializationError

"""<p>Pentest job step names.</p>"""
StepName: TypeAlias = Literal[
    "PREFLIGHT",
    "STATIC_ANALYSIS",
    "PENTEST",
    "FINALIZING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PREFLIGHT",
        "STATIC_ANALYSIS",
        "PENTEST",
        "FINALIZING",
    )
)


def serialize_json(value: StepName) -> str:
    return value


def deserialize_json(data: str) -> StepName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StepName value: {data!r}")
    return cast(StepName, data)
