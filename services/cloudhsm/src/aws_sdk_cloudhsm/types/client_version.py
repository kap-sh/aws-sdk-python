"""Generated from Smithy shape ``com.amazonaws.cloudhsm#ClientVersion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudhsm.errors import DeserializationError

ClientVersion: TypeAlias = Literal[
    "5.1",
    "5.3",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "5.1",
        "5.3",
    )
)


def serialize_aws_json_1_1(value: ClientVersion) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ClientVersion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientVersion value: {data!r}")
    return cast(ClientVersion, data)
