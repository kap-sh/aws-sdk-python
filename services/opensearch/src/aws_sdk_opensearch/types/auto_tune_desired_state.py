"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneDesiredState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>The Auto-Tune desired state. Valid values are ENABLED and DISABLED.</p>"""
AutoTuneDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: AutoTuneDesiredState) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneDesiredState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoTuneDesiredState value: {data!r}")
    return cast(AutoTuneDesiredState, data)
