"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#Decision``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

Decision: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_aws_json_1_0(value: Decision) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Decision:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Decision value: {data!r}")
    return cast(Decision, data)
