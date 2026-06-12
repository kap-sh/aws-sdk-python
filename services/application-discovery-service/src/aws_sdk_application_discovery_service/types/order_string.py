"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#orderString``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_discovery_service.errors import DeserializationError

orderString: TypeAlias = Literal[
    "ASC",
    "DESC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ASC",
        "DESC",
    )
)


def serialize_aws_json_1_1(value: orderString) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> orderString:
    if data not in _VALUES:
        raise DeserializationError(f"unknown orderString value: {data!r}")
    return cast(orderString, data)
