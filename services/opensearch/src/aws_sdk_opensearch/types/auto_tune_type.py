"""Generated from Smithy shape ``com.amazonaws.opensearch#AutoTuneType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

"""<p>Specifies the Auto-Tune type. Valid value is SCHEDULED_ACTION.</p>"""
AutoTuneType: TypeAlias = Literal["SCHEDULED_ACTION",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SCHEDULED_ACTION",))


def serialize_json(value: AutoTuneType) -> str:
    return value


def deserialize_json(data: str) -> AutoTuneType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoTuneType value: {data!r}")
    return cast(AutoTuneType, data)
