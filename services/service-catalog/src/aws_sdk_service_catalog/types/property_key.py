"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PropertyKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

PropertyKey: TypeAlias = Literal[
    "OWNER",
    "LAUNCH_ROLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OWNER",
        "LAUNCH_ROLE",
    )
)


def serialize_aws_json_1_1(value: PropertyKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PropertyKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PropertyKey value: {data!r}")
    return cast(PropertyKey, data)
