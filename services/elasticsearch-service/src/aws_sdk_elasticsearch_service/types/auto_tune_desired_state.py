"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneDesiredState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticsearch_service.errors import DeserializationError

"""<p>Specifies the Auto-Tune desired state. Valid values are ENABLED, DISABLED.</p>"""
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
