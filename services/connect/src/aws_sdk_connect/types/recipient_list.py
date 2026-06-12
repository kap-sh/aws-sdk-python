"""Generated from Smithy shape ``com.amazonaws.connect#RecipientList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn

RecipientList: TypeAlias = list["aws_sdk_connect.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: RecipientList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecipientList:
    return list(data)
