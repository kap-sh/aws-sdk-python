"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DetailedErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_error

DetailedErrors: TypeAlias = list["capo_iotsitewise.types.detailed_error.DetailedError"]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedErrors) -> list:
    import capo_iotsitewise.types.detailed_error

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.detailed_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> DetailedErrors:
    import capo_iotsitewise.types.detailed_error

    out: DetailedErrors = []
    for item in data:
        out.append(capo_iotsitewise.types.detailed_error.deserialize_json(item))
    return out
