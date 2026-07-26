"""Generated from Smithy shape ``com.amazonaws.detective#UnprocessedAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_detective.types.unprocessed_account

UnprocessedAccountList: TypeAlias = list[
    "capo_detective.types.unprocessed_account.UnprocessedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAccountList) -> list:
    import capo_detective.types.unprocessed_account

    out: list = []
    for item in value:
        out.append(capo_detective.types.unprocessed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedAccountList:
    import capo_detective.types.unprocessed_account

    out: UnprocessedAccountList = []
    for item in data:
        out.append(capo_detective.types.unprocessed_account.deserialize_json(item))
    return out
