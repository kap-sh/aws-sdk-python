"""Generated from Smithy shape ``com.amazonaws.clouddirectory#Arns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.arn

Arns: TypeAlias = list["aws_sdk_clouddirectory.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: Arns) -> list:
    return list(value)


def deserialize_json(data: list) -> Arns:
    return list(data)
