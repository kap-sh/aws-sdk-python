"""Generated from Smithy shape ``com.amazonaws.lambda#SourceAccessType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_lambda.errors import DeserializationError

SourceAccessType: TypeAlias = Literal[
    "BASIC_AUTH",
    "VPC_SUBNET",
    "VPC_SECURITY_GROUP",
    "SASL_SCRAM_512_AUTH",
    "SASL_SCRAM_256_AUTH",
    "VIRTUAL_HOST",
    "CLIENT_CERTIFICATE_TLS_AUTH",
    "SERVER_ROOT_CA_CERTIFICATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC_AUTH",
        "VPC_SUBNET",
        "VPC_SECURITY_GROUP",
        "SASL_SCRAM_512_AUTH",
        "SASL_SCRAM_256_AUTH",
        "VIRTUAL_HOST",
        "CLIENT_CERTIFICATE_TLS_AUTH",
        "SERVER_ROOT_CA_CERTIFICATE",
    )
)


def serialize_json(value: SourceAccessType) -> str:
    return value


def deserialize_json(data: str) -> SourceAccessType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceAccessType value: {data!r}")
    return cast(SourceAccessType, data)
