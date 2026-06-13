"""Generated from Smithy shape ``com.amazonaws.location#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.arn

ArnList: TypeAlias = list["aws_sdk_location.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
