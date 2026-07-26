"""Generated from Smithy shape ``com.amazonaws.connect#FailedRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.failed_request

FailedRequestList: TypeAlias = list["capo_connect.types.failed_request.FailedRequest"]


# --- restJson1 ser/de ---
def serialize_json(value: FailedRequestList) -> list:
    import capo_connect.types.failed_request

    out: list = []
    for item in value:
        out.append(capo_connect.types.failed_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedRequestList:
    import capo_connect.types.failed_request

    out: FailedRequestList = []
    for item in data:
        out.append(capo_connect.types.failed_request.deserialize_json(item))
    return out
