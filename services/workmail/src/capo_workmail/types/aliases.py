"""Generated from Smithy shape ``com.amazonaws.workmail#Aliases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workmail.types.email_address

Aliases: TypeAlias = list["capo_workmail.types.email_address.EmailAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Aliases) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Aliases:
    return list(data)
