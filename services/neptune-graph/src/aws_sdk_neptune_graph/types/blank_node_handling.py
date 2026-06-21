"""Generated from Smithy shape ``com.amazonaws.neptunegraph#BlankNodeHandling``."""

from typing import Literal, TypeAlias, cast

BlankNodeHandling: TypeAlias = Literal["convertToIri",]


# --- restJson1 ser/de ---
def serialize_json(value: BlankNodeHandling) -> str:
    return value


def deserialize_json(data: str) -> BlankNodeHandling:
    return cast(BlankNodeHandling, data)
