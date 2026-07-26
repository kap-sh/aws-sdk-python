"""Generated from Smithy shape ``com.amazonaws.macie2#__listOfUnprocessedAccount``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.unprocessed_account

__listOfUnprocessedAccount: TypeAlias = list[
    "capo_macie2.types.unprocessed_account.UnprocessedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfUnprocessedAccount) -> list:
    import capo_macie2.types.unprocessed_account

    out: list = []
    for item in value:
        out.append(capo_macie2.types.unprocessed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfUnprocessedAccount:
    import capo_macie2.types.unprocessed_account

    out: __listOfUnprocessedAccount = []
    for item in data:
        out.append(capo_macie2.types.unprocessed_account.deserialize_json(item))
    return out
