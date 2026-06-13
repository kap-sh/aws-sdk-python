"""Generated from Smithy shape ``com.amazonaws.backup#LegalHoldsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.legal_hold

LegalHoldsList: TypeAlias = list["aws_sdk_backup.types.legal_hold.LegalHold"]


# --- restJson1 ser/de ---
def serialize_json(value: LegalHoldsList) -> list:
    import aws_sdk_backup.types.legal_hold

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.legal_hold.serialize_json(item))
    return out


def deserialize_json(data: list) -> LegalHoldsList:
    import aws_sdk_backup.types.legal_hold

    out: LegalHoldsList = []
    for item in data:
        out.append(aws_sdk_backup.types.legal_hold.deserialize_json(item))
    return out
