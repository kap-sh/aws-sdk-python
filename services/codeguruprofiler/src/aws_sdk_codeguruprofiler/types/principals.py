"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Principals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.principal

Principals: TypeAlias = list["aws_sdk_codeguruprofiler.types.principal.Principal"]


# --- restJson1 ser/de ---
def serialize_json(value: Principals) -> list:
    return list(value)


def deserialize_json(data: list) -> Principals:
    return list(data)
