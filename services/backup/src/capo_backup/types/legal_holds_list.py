"""Generated from Smithy shape ``com.amazonaws.backup#LegalHoldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.legal_hold

LegalHoldsList: TypeAlias = list["capo_backup.types.legal_hold.LegalHold"]


# --- restJson1 ser/de ---
def serialize_json(value: LegalHoldsList) -> list:
    import capo_backup.types.legal_hold

    out: list = []
    for item in value:
        out.append(capo_backup.types.legal_hold.serialize_json(item))
    return out


def deserialize_json(data: list) -> LegalHoldsList:
    import capo_backup.types.legal_hold

    out: LegalHoldsList = []
    for item in data:
        out.append(capo_backup.types.legal_hold.deserialize_json(item))
    return out
