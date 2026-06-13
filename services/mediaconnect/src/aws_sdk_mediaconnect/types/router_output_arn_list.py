"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterOutputArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_output_arn

RouterOutputArnList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_output_arn.RouterOutputArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterOutputArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RouterOutputArnList:
    return list(data)
