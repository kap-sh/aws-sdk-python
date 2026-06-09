"""Generated from Smithy shape ``com.amazonaws.kms#DataKeySpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

DataKeySpec: TypeAlias = Literal[
    "AES_256",
    "AES_128",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AES_256",
        "AES_128",
    )
)


def serialize_aws_json_1_1(value: DataKeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataKeySpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataKeySpec value: {data!r}")
    return cast(DataKeySpec, data)
