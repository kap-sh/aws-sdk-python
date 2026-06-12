"""Generated from Smithy shape ``com.amazonaws.fsx#AutoImportPolicyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

AutoImportPolicyType: TypeAlias = Literal[
    "NONE",
    "NEW",
    "NEW_CHANGED",
    "NEW_CHANGED_DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "NEW",
        "NEW_CHANGED",
        "NEW_CHANGED_DELETED",
    )
)


def serialize_aws_json_1_1(value: AutoImportPolicyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoImportPolicyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoImportPolicyType value: {data!r}")
    return cast(AutoImportPolicyType, data)
