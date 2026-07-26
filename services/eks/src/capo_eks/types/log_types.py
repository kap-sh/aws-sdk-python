"""Generated from Smithy shape ``com.amazonaws.eks#LogTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.log_type

LogTypes: TypeAlias = list["capo_eks.types.log_type.LogType"]


# --- restJson1 ser/de ---
def serialize_json(value: LogTypes) -> list:
    import capo_eks.types.log_type

    out: list = []
    for item in value:
        out.append(capo_eks.types.log_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogTypes:
    import capo_eks.types.log_type

    out: LogTypes = []
    for item in data:
        out.append(capo_eks.types.log_type.deserialize_json(item))
    return out
