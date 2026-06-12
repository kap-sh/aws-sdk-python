"""Generated from Smithy shape ``com.amazonaws.wafv2#DataProtectionAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_wafv2.errors import DeserializationError

DataProtectionAction: TypeAlias = Literal[
    "SUBSTITUTION",
    "HASH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUBSTITUTION",
        "HASH",
    )
)


def serialize_aws_json_1_1(value: DataProtectionAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataProtectionAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataProtectionAction value: {data!r}")
    return cast(DataProtectionAction, data)
