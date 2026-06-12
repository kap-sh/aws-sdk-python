"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_metadata

EmailAddressList: TypeAlias = list[
    "aws_sdk_connect.types.email_address_metadata.EmailAddressMetadata"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressList) -> list:
    import aws_sdk_connect.types.email_address_metadata

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.email_address_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressList:
    import aws_sdk_connect.types.email_address_metadata

    out: EmailAddressList = []
    for item in data:
        out.append(aws_sdk_connect.types.email_address_metadata.deserialize_json(item))
    return out
