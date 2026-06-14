"""Generated from Smithy shape ``com.amazonaws.workspaces#EndpointEncryptionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

EndpointEncryptionMode: TypeAlias = Literal[
    "STANDARD_TLS",
    "FIPS_VALIDATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD_TLS",
        "FIPS_VALIDATED",
    )
)


def serialize_aws_json_1_1(value: EndpointEncryptionMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EndpointEncryptionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EndpointEncryptionMode value: {data!r}")
    return cast(EndpointEncryptionMode, data)
