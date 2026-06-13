"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

RuleResultStatus: TypeAlias = Literal[
    "PASSED",
    "FAILED",
    "WARNING",
    "INFO",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSED",
        "FAILED",
        "WARNING",
        "INFO",
        "UNKNOWN",
    )
)


def serialize_json(value: RuleResultStatus) -> str:
    return value


def deserialize_json(data: str) -> RuleResultStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RuleResultStatus value: {data!r}")
    return cast(RuleResultStatus, data)
