"""Generated from Smithy shape ``com.amazonaws.guardduty#UnprocessedAccounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.unprocessed_account

UnprocessedAccounts: TypeAlias = list[
    "capo_guardduty.types.unprocessed_account.UnprocessedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAccounts) -> list:
    import capo_guardduty.types.unprocessed_account

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.unprocessed_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> UnprocessedAccounts:
    import capo_guardduty.types.unprocessed_account

    out: UnprocessedAccounts = []
    for item in data:
        out.append(capo_guardduty.types.unprocessed_account.deserialize_json(item))
    return out
