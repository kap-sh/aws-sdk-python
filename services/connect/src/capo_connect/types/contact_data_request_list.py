"""Generated from Smithy shape ``com.amazonaws.connect#ContactDataRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_data_request

ContactDataRequestList: TypeAlias = list[
    "capo_connect.types.contact_data_request.ContactDataRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactDataRequestList) -> list:
    import capo_connect.types.contact_data_request

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_data_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactDataRequestList:
    import capo_connect.types.contact_data_request

    out: ContactDataRequestList = []
    for item in data:
        out.append(capo_connect.types.contact_data_request.deserialize_json(item))
    return out
