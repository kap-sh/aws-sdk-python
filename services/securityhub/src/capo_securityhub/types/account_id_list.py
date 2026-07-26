"""Generated from Smithy shape ``com.amazonaws.securityhub#AccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

AccountIdList: TypeAlias = list[
    "capo_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AccountIdList:
    return list(data)
