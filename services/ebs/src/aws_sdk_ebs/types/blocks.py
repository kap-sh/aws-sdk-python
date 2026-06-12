"""Generated from Smithy shape ``com.amazonaws.ebs#Blocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ebs.types.block

Blocks: TypeAlias = list["aws_sdk_ebs.types.block.Block"]


# --- restJson1 ser/de ---
def serialize_json(value: Blocks) -> list:
    import aws_sdk_ebs.types.block

    out: list = []
    for item in value:
        out.append(aws_sdk_ebs.types.block.serialize_json(item))
    return out


def deserialize_json(data: list) -> Blocks:
    import aws_sdk_ebs.types.block

    out: Blocks = []
    for item in data:
        out.append(aws_sdk_ebs.types.block.deserialize_json(item))
    return out
