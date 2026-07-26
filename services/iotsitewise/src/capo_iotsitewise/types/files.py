"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Files``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.file

Files: TypeAlias = list["capo_iotsitewise.types.file.File"]


# --- restJson1 ser/de ---
def serialize_json(value: Files) -> list:
    import capo_iotsitewise.types.file

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.file.serialize_json(item))
    return out


def deserialize_json(data: list) -> Files:
    import capo_iotsitewise.types.file

    out: Files = []
    for item in data:
        out.append(capo_iotsitewise.types.file.deserialize_json(item))
    return out
