"""Generated from Smithy shape ``com.amazonaws.emrcontainers#TagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr_containers.types.string128

TagKeyList: TypeAlias = list["capo_emr_containers.types.string128.String128"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeyList) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeyList:
    return list(data)
