"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfIpPoolUpdateRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.ip_pool_update_request

__listOfIpPoolUpdateRequest: TypeAlias = list[
    "capo_medialive.types.ip_pool_update_request.IpPoolUpdateRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfIpPoolUpdateRequest) -> list:
    import capo_medialive.types.ip_pool_update_request

    out: list = []
    for item in value:
        out.append(capo_medialive.types.ip_pool_update_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfIpPoolUpdateRequest:
    import capo_medialive.types.ip_pool_update_request

    out: __listOfIpPoolUpdateRequest = []
    for item in data:
        out.append(capo_medialive.types.ip_pool_update_request.deserialize_json(item))
    return out
