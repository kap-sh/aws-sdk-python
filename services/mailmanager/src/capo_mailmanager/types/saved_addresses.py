"""Generated from Smithy shape ``com.amazonaws.mailmanager#SavedAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.saved_address

SavedAddresses: TypeAlias = list["capo_mailmanager.types.saved_address.SavedAddress"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SavedAddresses) -> list:
    import capo_mailmanager.types.saved_address

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.saved_address.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SavedAddresses:
    import capo_mailmanager.types.saved_address

    out: SavedAddresses = []
    for item in data:
        out.append(capo_mailmanager.types.saved_address.deserialize_aws_json_1_0(item))
    return out
