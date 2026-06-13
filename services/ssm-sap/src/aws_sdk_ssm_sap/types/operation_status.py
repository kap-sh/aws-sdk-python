"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "INPROGRESS",
    "SUCCESS",
    "ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INPROGRESS",
        "SUCCESS",
        "ERROR",
    )
)


def serialize_json(value: OperationStatus) -> str:
    return value


def deserialize_json(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
