"""Generated from Smithy shape ``com.amazonaws.fms#CustomerPolicyScopeIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

CustomerPolicyScopeIdType: TypeAlias = Literal[
    "ACCOUNT",
    "ORG_UNIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT",
        "ORG_UNIT",
    )
)


def serialize_aws_json_1_1(value: CustomerPolicyScopeIdType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomerPolicyScopeIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerPolicyScopeIdType value: {data!r}")
    return cast(CustomerPolicyScopeIdType, data)
