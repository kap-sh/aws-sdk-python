"""Generated from Smithy shape ``com.amazonaws.groundstation#ContactList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.contact_data

ContactList: TypeAlias = list["aws_sdk_groundstation.types.contact_data.ContactData"]


# --- restJson1 ser/de ---
def serialize_json(value: ContactList) -> list:
    import aws_sdk_groundstation.types.contact_data

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.contact_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactList:
    import aws_sdk_groundstation.types.contact_data

    out: ContactList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.contact_data.deserialize_json(item))
    return out
