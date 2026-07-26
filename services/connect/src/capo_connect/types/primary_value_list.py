"""Generated from Smithy shape ``com.amazonaws.connect#PrimaryValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.iam_restricted_primary_value

PrimaryValueList: TypeAlias = list[
    "capo_connect.types.iam_restricted_primary_value.IAMRestrictedPrimaryValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PrimaryValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrimaryValueList:
    return list(data)
