"""Generated from Smithy shape ``com.amazonaws.healthlake#AuthorizationStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_healthlake.errors import DeserializationError

AuthorizationStrategy: TypeAlias = Literal[
    "SMART_ON_FHIR_V1",
    "SMART_ON_FHIR",
    "AWS_AUTH",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SMART_ON_FHIR_V1",
        "SMART_ON_FHIR",
        "AWS_AUTH",
    )
)


def serialize_aws_json_1_0(value: AuthorizationStrategy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AuthorizationStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizationStrategy value: {data!r}")
    return cast(AuthorizationStrategy, data)
