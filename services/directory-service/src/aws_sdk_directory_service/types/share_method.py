"""Generated from Smithy shape ``com.amazonaws.directoryservice#ShareMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

ShareMethod: TypeAlias = Literal[
    "ORGANIZATIONS",
    "HANDSHAKE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ORGANIZATIONS",
        "HANDSHAKE",
    )
)


def serialize_aws_json_1_1(value: ShareMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ShareMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareMethod value: {data!r}")
    return cast(ShareMethod, data)
