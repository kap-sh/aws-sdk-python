"""Generated from Smithy shape ``com.amazonaws.mailmanager#Recipients``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.email_address

Recipients: TypeAlias = list["aws_sdk_mailmanager.types.email_address.EmailAddress"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Recipients) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> Recipients:
    return list(data)
