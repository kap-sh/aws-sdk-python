"""Generated from Smithy shape ``com.amazonaws.workdocs#SharedLabels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.shared_label

SharedLabels: TypeAlias = list["capo_workdocs.types.shared_label.SharedLabel"]


# --- restJson1 ser/de ---
def serialize_json(value: SharedLabels) -> list:
    return list(value)


def deserialize_json(data: list) -> SharedLabels:
    return list(data)
