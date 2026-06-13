"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConnectedEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ConnectedEntityType: TypeAlias = Literal["DBMS",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DBMS",))


def serialize_json(value: ConnectedEntityType) -> str:
    return value


def deserialize_json(data: str) -> ConnectedEntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectedEntityType value: {data!r}")
    return cast(ConnectedEntityType, data)
