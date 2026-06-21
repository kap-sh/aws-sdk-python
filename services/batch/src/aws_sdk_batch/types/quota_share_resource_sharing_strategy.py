"""Generated from Smithy shape ``com.amazonaws.batch#QuotaShareResourceSharingStrategy``."""

from typing import Literal, TypeAlias, cast

QuotaShareResourceSharingStrategy: TypeAlias = Literal[
    "RESERVE",
    "LEND",
    "LEND_AND_BORROW",
]


# --- restJson1 ser/de ---
def serialize_json(value: QuotaShareResourceSharingStrategy) -> str:
    return value


def deserialize_json(data: str) -> QuotaShareResourceSharingStrategy:
    return cast(QuotaShareResourceSharingStrategy, data)
