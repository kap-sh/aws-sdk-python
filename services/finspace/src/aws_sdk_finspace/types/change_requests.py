"""Generated from Smithy shape ``com.amazonaws.finspace#ChangeRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_finspace.types.change_request

ChangeRequests: TypeAlias = list["aws_sdk_finspace.types.change_request.ChangeRequest"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeRequests) -> list:
    import aws_sdk_finspace.types.change_request

    out: list = []
    for item in value:
        out.append(aws_sdk_finspace.types.change_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeRequests:
    import aws_sdk_finspace.types.change_request

    out: ChangeRequests = []
    for item in data:
        out.append(aws_sdk_finspace.types.change_request.deserialize_json(item))
    return out
