"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ClientAffinity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_global_accelerator.errors import DeserializationError

ClientAffinity: TypeAlias = Literal[
    "NONE",
    "SOURCE_IP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "SOURCE_IP",
    )
)


def serialize_aws_json_1_1(value: ClientAffinity) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientAffinity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientAffinity value: {data!r}")
    return cast(ClientAffinity, data)
