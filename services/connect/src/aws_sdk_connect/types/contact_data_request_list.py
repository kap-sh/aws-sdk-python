"""Generated from Smithy shape ``com.amazonaws.connect#ContactDataRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_data_request

ContactDataRequestList: TypeAlias = list[
    "aws_sdk_connect.types.contact_data_request.ContactDataRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactDataRequestList) -> list:
    import aws_sdk_connect.types.contact_data_request

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.contact_data_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactDataRequestList:
    import aws_sdk_connect.types.contact_data_request

    out: ContactDataRequestList = []
    for item in data:
        out.append(aws_sdk_connect.types.contact_data_request.deserialize_json(item))
    return out
