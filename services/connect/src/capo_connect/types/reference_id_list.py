"""Generated from Smithy shape ``com.amazonaws.connect#ReferenceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.reference_id

ReferenceIdList: TypeAlias = list["capo_connect.types.reference_id.ReferenceId"]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ReferenceIdList:
    return list(data)
