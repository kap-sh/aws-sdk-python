"""Generated from Smithy shape ``com.amazonaws.organizations#PolicyTypeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_organizations.errors import DeserializationError

PolicyTypeStatus: TypeAlias = Literal[
    "ENABLED",
    "PENDING_ENABLE",
    "PENDING_DISABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "PENDING_ENABLE",
        "PENDING_DISABLE",
    )
)


def serialize_aws_json_1_1(value: PolicyTypeStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PolicyTypeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyTypeStatus value: {data!r}")
    return cast(PolicyTypeStatus, data)
