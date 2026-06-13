"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_input_arn

RouterInputArnList: TypeAlias = list[
    "aws_sdk_mediaconnect.types.router_input_arn.RouterInputArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> RouterInputArnList:
    return list(data)
