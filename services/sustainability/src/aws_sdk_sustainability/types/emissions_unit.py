"""Generated from Smithy shape ``com.amazonaws.sustainability#EmissionsUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sustainability.errors import DeserializationError

"""<p>Specifies the unit of measurement for emissions.</p>"""
EmissionsUnit: TypeAlias = Literal["MTCO2e",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("MTCO2e",))


def serialize_json(value: EmissionsUnit) -> str:
    return value


def deserialize_json(data: str) -> EmissionsUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmissionsUnit value: {data!r}")
    return cast(EmissionsUnit, data)
