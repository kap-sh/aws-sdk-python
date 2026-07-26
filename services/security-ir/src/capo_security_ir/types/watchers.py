"""Generated from Smithy shape ``com.amazonaws.securityir#Watchers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.watcher

Watchers: TypeAlias = list["capo_security_ir.types.watcher.Watcher"]


# --- restJson1 ser/de ---
def serialize_json(value: Watchers) -> list:
    import capo_security_ir.types.watcher

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.watcher.serialize_json(item))
    return out


def deserialize_json(data: list) -> Watchers:
    import capo_security_ir.types.watcher

    out: Watchers = []
    for item in data:
        out.append(capo_security_ir.types.watcher.deserialize_json(item))
    return out
