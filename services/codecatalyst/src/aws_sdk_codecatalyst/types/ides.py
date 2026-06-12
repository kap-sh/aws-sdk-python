"""Generated from Smithy shape ``com.amazonaws.codecatalyst#Ides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.ide

Ides: TypeAlias = list["aws_sdk_codecatalyst.types.ide.Ide"]


# --- restJson1 ser/de ---
def serialize_json(value: Ides) -> list:
    import aws_sdk_codecatalyst.types.ide

    out: list = []
    for item in value:
        out.append(aws_sdk_codecatalyst.types.ide.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ides:
    import aws_sdk_codecatalyst.types.ide

    out: Ides = []
    for item in data:
        out.append(aws_sdk_codecatalyst.types.ide.deserialize_json(item))
    return out
