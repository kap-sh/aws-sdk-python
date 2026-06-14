"""Generated from Smithy shape ``com.amazonaws.datazone#DomainUnitDesignation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

DomainUnitDesignation: TypeAlias = Literal["OWNER",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("OWNER",))


def serialize_json(value: DomainUnitDesignation) -> str:
    return value


def deserialize_json(data: str) -> DomainUnitDesignation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DomainUnitDesignation value: {data!r}")
    return cast(DomainUnitDesignation, data)
