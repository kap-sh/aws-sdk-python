"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#Owners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.owner

Owners: TypeAlias = list["capo_codeguru_reviewer.types.owner.Owner"]


# --- restJson1 ser/de ---
def serialize_json(value: Owners) -> list:
    return list(value)


def deserialize_json(data: list) -> Owners:
    return list(data)
