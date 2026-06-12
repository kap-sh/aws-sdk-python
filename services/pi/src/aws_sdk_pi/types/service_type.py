"""Generated from Smithy shape ``com.amazonaws.pi#ServiceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pi.errors import DeserializationError

ServiceType: TypeAlias = Literal[
    "RDS",
    "DOCDB",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RDS",
        "DOCDB",
    )
)


def serialize_aws_json_1_1(value: ServiceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceType value: {data!r}")
    return cast(ServiceType, data)
