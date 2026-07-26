"""Generated from Smithy shape ``com.amazonaws.finspace#EnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.environment

EnvironmentList: TypeAlias = list["capo_finspace.types.environment.Environment"]


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentList) -> list:
    import capo_finspace.types.environment

    out: list = []
    for item in value:
        out.append(capo_finspace.types.environment.serialize_json(item))
    return out


def deserialize_json(data: list) -> EnvironmentList:
    import capo_finspace.types.environment

    out: EnvironmentList = []
    for item in data:
        out.append(capo_finspace.types.environment.deserialize_json(item))
    return out
