"""Generated from Smithy shape ``com.amazonaws.ssmsap#BackintMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

BackintMode: TypeAlias = Literal["AWSBackup",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("AWSBackup",))


def serialize_json(value: BackintMode) -> str:
    return value


def deserialize_json(data: str) -> BackintMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BackintMode value: {data!r}")
    return cast(BackintMode, data)
