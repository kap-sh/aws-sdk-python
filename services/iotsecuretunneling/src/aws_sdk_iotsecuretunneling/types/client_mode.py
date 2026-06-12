"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#ClientMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsecuretunneling.errors import DeserializationError

ClientMode: TypeAlias = Literal[
    "SOURCE",
    "DESTINATION",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE",
        "DESTINATION",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: ClientMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientMode value: {data!r}")
    return cast(ClientMode, data)
