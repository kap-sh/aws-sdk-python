"""Generated from Smithy shape ``com.amazonaws.auditmanager#ChangeLogs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.change_log

ChangeLogs: TypeAlias = list["capo_auditmanager.types.change_log.ChangeLog"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeLogs) -> list:
    import capo_auditmanager.types.change_log

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.change_log.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeLogs:
    import capo_auditmanager.types.change_log

    out: ChangeLogs = []
    for item in data:
        out.append(capo_auditmanager.types.change_log.deserialize_json(item))
    return out
