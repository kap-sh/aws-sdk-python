"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedKeyRegistrationEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.failed_key_registration_entry

FailedKeyRegistrationEntries: TypeAlias = list[
    "aws_sdk_quicksight.types.failed_key_registration_entry.FailedKeyRegistrationEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedKeyRegistrationEntries) -> list:
    import aws_sdk_quicksight.types.failed_key_registration_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.failed_key_registration_entry.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedKeyRegistrationEntries:
    import aws_sdk_quicksight.types.failed_key_registration_entry

    out: FailedKeyRegistrationEntries = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.failed_key_registration_entry.deserialize_json(
                item
            )
        )
    return out
