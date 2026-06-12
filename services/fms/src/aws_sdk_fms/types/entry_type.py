"""Generated from Smithy shape ``com.amazonaws.fms#EntryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

EntryType: TypeAlias = Literal[
    "FMS_MANAGED_FIRST_ENTRY",
    "FMS_MANAGED_LAST_ENTRY",
    "CUSTOM_ENTRY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FMS_MANAGED_FIRST_ENTRY",
        "FMS_MANAGED_LAST_ENTRY",
        "CUSTOM_ENTRY",
    )
)


def serialize_aws_json_1_1(value: EntryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntryType value: {data!r}")
    return cast(EntryType, data)
