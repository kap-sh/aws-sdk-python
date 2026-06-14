"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

PolicyType: TypeAlias = Literal[
    "STATIC",
    "TEMPLATE_LINKED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STATIC",
        "TEMPLATE_LINKED",
    )
)


def serialize_aws_json_1_0(value: PolicyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PolicyType value: {data!r}")
    return cast(PolicyType, data)
