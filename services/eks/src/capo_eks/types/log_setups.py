"""Generated from Smithy shape ``com.amazonaws.eks#LogSetups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.log_setup

LogSetups: TypeAlias = list["capo_eks.types.log_setup.LogSetup"]


# --- restJson1 ser/de ---
def serialize_json(value: LogSetups) -> list:
    import capo_eks.types.log_setup

    out: list = []
    for item in value:
        out.append(capo_eks.types.log_setup.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogSetups:
    import capo_eks.types.log_setup

    out: LogSetups = []
    for item in data:
        out.append(capo_eks.types.log_setup.deserialize_json(item))
    return out
