"""Generated from Smithy shape ``com.amazonaws.organizations#HandshakeState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

HandshakeState: TypeAlias = Literal[
    "REQUESTED",
    "OPEN",
    "CANCELED",
    "ACCEPTED",
    "DECLINED",
    "EXPIRED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REQUESTED",
        "OPEN",
        "CANCELED",
        "ACCEPTED",
        "DECLINED",
        "EXPIRED",
    )
)


def serialize_aws_json_1_1(value: HandshakeState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HandshakeState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HandshakeState value: {data!r}")
    return cast(HandshakeState, data)
