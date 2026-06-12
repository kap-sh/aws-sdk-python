"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#OfferingClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

OfferingClass: TypeAlias = Literal[
    "STANDARD",
    "CONVERTIBLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "CONVERTIBLE",
    )
)


def serialize_aws_json_1_1(value: OfferingClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferingClass value: {data!r}")
    return cast(OfferingClass, data)
