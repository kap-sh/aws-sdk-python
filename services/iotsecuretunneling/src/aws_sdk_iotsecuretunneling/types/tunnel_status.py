"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#TunnelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsecuretunneling.errors import DeserializationError

TunnelStatus: TypeAlias = Literal[
    "OPEN",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPEN",
        "CLOSED",
    )
)


def serialize_aws_json_1_1(value: TunnelStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TunnelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TunnelStatus value: {data!r}")
    return cast(TunnelStatus, data)
