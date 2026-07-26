"""Generated from Smithy shape ``com.amazonaws.mgn#ConflictExceptionErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.error_details

ConflictExceptionErrors: TypeAlias = list["capo_mgn.types.error_details.ErrorDetails"]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionErrors) -> list:
    import capo_mgn.types.error_details

    out: list = []
    for item in value:
        out.append(capo_mgn.types.error_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConflictExceptionErrors:
    import capo_mgn.types.error_details

    out: ConflictExceptionErrors = []
    for item in data:
        out.append(capo_mgn.types.error_details.deserialize_json(item))
    return out
