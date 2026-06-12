"""Generated from Smithy shape ``com.amazonaws.sesv2#AdditionalContactEmailAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.additional_contact_email_address

AdditionalContactEmailAddresses: TypeAlias = list[
    "aws_sdk_sesv2.types.additional_contact_email_address.AdditionalContactEmailAddress"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalContactEmailAddresses) -> list:
    return list(value)


def deserialize_json(data: list) -> AdditionalContactEmailAddresses:
    return list(data)
