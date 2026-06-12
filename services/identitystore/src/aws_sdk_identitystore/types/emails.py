"""Generated from Smithy shape ``com.amazonaws.identitystore#Emails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_identitystore.types.email

Emails: TypeAlias = list["aws_sdk_identitystore.types.email.Email"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Emails) -> list:
    import aws_sdk_identitystore.types.email

    out: list = []
    for item in value:
        out.append(aws_sdk_identitystore.types.email.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Emails:
    import aws_sdk_identitystore.types.email

    out: Emails = []
    for item in data:
        out.append(aws_sdk_identitystore.types.email.deserialize_aws_json_1_1(item))
    return out
