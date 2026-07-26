"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressMetadataList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.email_address_summary

EmailAddressMetadataList: TypeAlias = list[
    "capo_connect.types.email_address_summary.EmailAddressSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressMetadataList) -> list:
    import capo_connect.types.email_address_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.email_address_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EmailAddressMetadataList:
    import capo_connect.types.email_address_summary

    out: EmailAddressMetadataList = []
    for item in data:
        out.append(capo_connect.types.email_address_summary.deserialize_json(item))
    return out
