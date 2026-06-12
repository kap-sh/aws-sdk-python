"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingInstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.blocking_instance

BlockingInstancesList: TypeAlias = list[
    "aws_sdk_outposts.types.blocking_instance.BlockingInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockingInstancesList) -> list:
    import aws_sdk_outposts.types.blocking_instance

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.blocking_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockingInstancesList:
    import aws_sdk_outposts.types.blocking_instance

    out: BlockingInstancesList = []
    for item in data:
        out.append(aws_sdk_outposts.types.blocking_instance.deserialize_json(item))
    return out
