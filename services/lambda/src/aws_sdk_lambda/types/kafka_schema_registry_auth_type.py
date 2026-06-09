"""Generated from Smithy shape ``com.amazonaws.lambda#KafkaSchemaRegistryAuthType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

KafkaSchemaRegistryAuthType: TypeAlias = Literal[
    "BASIC_AUTH",
    "CLIENT_CERTIFICATE_TLS_AUTH",
    "SERVER_ROOT_CA_CERTIFICATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC_AUTH",
        "CLIENT_CERTIFICATE_TLS_AUTH",
        "SERVER_ROOT_CA_CERTIFICATE",
    )
)


def serialize_json(value: KafkaSchemaRegistryAuthType) -> str:
    return value


def deserialize_json(data: str) -> KafkaSchemaRegistryAuthType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KafkaSchemaRegistryAuthType value: {data!r}"
        )
    return cast(KafkaSchemaRegistryAuthType, data)
