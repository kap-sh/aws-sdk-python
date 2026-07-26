"""Generated from Smithy shape ``com.amazonaws.imagebuilder#AmiList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.ami

AmiList: TypeAlias = list["capo_imagebuilder.types.ami.Ami"]


# --- restJson1 ser/de ---
def serialize_json(value: AmiList) -> list:
    import capo_imagebuilder.types.ami

    out: list = []
    for item in value:
        out.append(capo_imagebuilder.types.ami.serialize_json(item))
    return out


def deserialize_json(data: list) -> AmiList:
    import capo_imagebuilder.types.ami

    out: AmiList = []
    for item in data:
        out.append(capo_imagebuilder.types.ami.deserialize_json(item))
    return out
