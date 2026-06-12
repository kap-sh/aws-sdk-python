"""Generated from Smithy shape ``com.amazonaws.directoryservice#TrustType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

TrustType: TypeAlias = Literal[
    "Forest",
    "External",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Forest",
        "External",
    )
)


def serialize_aws_json_1_1(value: TrustType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrustType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TrustType value: {data!r}")
    return cast(TrustType, data)
