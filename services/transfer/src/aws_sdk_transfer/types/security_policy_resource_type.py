"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

SecurityPolicyResourceType: TypeAlias = Literal[
    "SERVER",
    "CONNECTOR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVER",
        "CONNECTOR",
    )
)


def serialize_aws_json_1_1(value: SecurityPolicyResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityPolicyResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SecurityPolicyResourceType value: {data!r}"
        )
    return cast(SecurityPolicyResourceType, data)
