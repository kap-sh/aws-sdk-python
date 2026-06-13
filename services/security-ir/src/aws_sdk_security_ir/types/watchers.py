"""Generated from Smithy shape ``com.amazonaws.securityir#Watchers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.watcher

Watchers: TypeAlias = list["aws_sdk_security_ir.types.watcher.Watcher"]


# --- restJson1 ser/de ---
def serialize_json(value: Watchers) -> list:
    import aws_sdk_security_ir.types.watcher

    out: list = []
    for item in value:
        out.append(aws_sdk_security_ir.types.watcher.serialize_json(item))
    return out


def deserialize_json(data: list) -> Watchers:
    import aws_sdk_security_ir.types.watcher

    out: Watchers = []
    for item in data:
        out.append(aws_sdk_security_ir.types.watcher.deserialize_json(item))
    return out
