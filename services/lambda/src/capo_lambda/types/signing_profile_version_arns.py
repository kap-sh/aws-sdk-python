"""Generated from Smithy shape ``com.amazonaws.lambda#SigningProfileVersionArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.arn

SigningProfileVersionArns: TypeAlias = list["capo_lambda.types.arn.Arn"]


# --- restJson1 ser/de ---
def serialize_json(value: SigningProfileVersionArns) -> list:
    return list(value)


def deserialize_json(data: list) -> SigningProfileVersionArns:
    return [item for item in data if item is not None]
