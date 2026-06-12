"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#KafkaSslEndpointIdentificationAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

KafkaSslEndpointIdentificationAlgorithm: TypeAlias = Literal[
    "none",
    "https",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "https",
    )
)


def serialize_aws_json_1_1(value: KafkaSslEndpointIdentificationAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KafkaSslEndpointIdentificationAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown KafkaSslEndpointIdentificationAlgorithm value: {data!r}"
        )
    return cast(KafkaSslEndpointIdentificationAlgorithm, data)
