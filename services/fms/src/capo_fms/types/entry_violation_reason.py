"""Generated from Smithy shape ``com.amazonaws.fms#EntryViolationReason``."""

from typing import Literal, TypeAlias, cast

EntryViolationReason: TypeAlias = Literal[
    "MISSING_EXPECTED_ENTRY",
    "INCORRECT_ENTRY_ORDER",
    "ENTRY_CONFLICT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryViolationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntryViolationReason:
    return cast(EntryViolationReason, data)
