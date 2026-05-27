"""Generated from Smithy shape ``com.amazonaws.lambda#SigningProfileVersionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.arn

SigningProfileVersionArns: TypeAlias = list["aws_sdk_lambda.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfileVersionArns) -> list:
    return list(value)


def deserialize_json(data: list) -> SigningProfileVersionArns:
    return list(data)
