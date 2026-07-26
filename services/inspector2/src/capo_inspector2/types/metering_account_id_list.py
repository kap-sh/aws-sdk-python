"""Generated from Smithy shape ``com.amazonaws.inspector2#MeteringAccountIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.metering_account_id

MeteringAccountIdList: TypeAlias = list[
    "capo_inspector2.types.metering_account_id.MeteringAccountId"
]


# --- restJson1 ser/de ---
def serialize_json(value: MeteringAccountIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> MeteringAccountIdList:
    return list(data)
