"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolationReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

EntryViolationReason: TypeAlias = Literal[
    "MISSING_EXPECTED_ENTRY",
    "INCORRECT_ENTRY_ORDER",
    "ENTRY_CONFLICT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MISSING_EXPECTED_ENTRY",
        "INCORRECT_ENTRY_ORDER",
        "ENTRY_CONFLICT",
    )
)


def serialize_aws_json_1_1(value: EntryViolationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntryViolationReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntryViolationReason value: {data!r}")
    return cast(EntryViolationReason, data)
