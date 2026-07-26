"""Generated from Smithy shape ``com.amazonaws.finspace#ChangeRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_finspace.types.change_request

ChangeRequests: TypeAlias = list["capo_finspace.types.change_request.ChangeRequest"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeRequests) -> list:
    import capo_finspace.types.change_request

    out: list = []
    for item in value:
        out.append(capo_finspace.types.change_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeRequests:
    import capo_finspace.types.change_request

    out: ChangeRequests = []
    for item in data:
        out.append(capo_finspace.types.change_request.deserialize_json(item))
    return out
