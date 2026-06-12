"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.email_address_summary

EmailAddressMetadataList: TypeAlias = list[
    "aws_sdk_connect.types.email_address_summary.EmailAddressSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressMetadataList) -> list:
    import aws_sdk_connect.types.email_address_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.email_address_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressMetadataList:
    import aws_sdk_connect.types.email_address_summary

    out: EmailAddressMetadataList = []
    for item in data:
        out.append(aws_sdk_connect.types.email_address_summary.deserialize_json(item))
    return out
