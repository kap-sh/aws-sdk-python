"""Generated from Smithy shape ``com.amazonaws.drs#Cpus``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_drs.types.cpu

Cpus: TypeAlias = list["aws_sdk_drs.types.cpu.CPU"]


# --- restJson1 ser/de ---
def serialize_json(value: Cpus) -> list:
    import aws_sdk_drs.types.cpu

    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.cpu.serialize_json(item))
    return out


def deserialize_json(data: list) -> Cpus:
    import aws_sdk_drs.types.cpu

    out: Cpus = []
    for item in data:
        out.append(aws_sdk_drs.types.cpu.deserialize_json(item))
    return out
