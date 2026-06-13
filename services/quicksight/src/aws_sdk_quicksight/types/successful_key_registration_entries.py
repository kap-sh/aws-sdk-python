"""Generated from Smithy shape ``com.amazonaws.quicksight#SuccessfulKeyRegistrationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.successful_key_registration_entry

SuccessfulKeyRegistrationEntries: TypeAlias = list[
    "aws_sdk_quicksight.types.successful_key_registration_entry.SuccessfulKeyRegistrationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulKeyRegistrationEntries) -> list:
    import aws_sdk_quicksight.types.successful_key_registration_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.successful_key_registration_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SuccessfulKeyRegistrationEntries:
    import aws_sdk_quicksight.types.successful_key_registration_entry

    out: SuccessfulKeyRegistrationEntries = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.successful_key_registration_entry.deserialize_json(
                item
            )
        )
    return out
