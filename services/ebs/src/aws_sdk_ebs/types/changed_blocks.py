"""Generated from Smithy shape ``com.amazonaws.ebs#ChangedBlocks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ebs.types.changed_block

ChangedBlocks: TypeAlias = list["aws_sdk_ebs.types.changed_block.ChangedBlock"]


# --- restJson1 ser/de ---
def serialize_json(value: ChangedBlocks) -> list:
    import aws_sdk_ebs.types.changed_block

    out: list = []
    for item in value:
        out.append(aws_sdk_ebs.types.changed_block.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangedBlocks:
    import aws_sdk_ebs.types.changed_block

    out: ChangedBlocks = []
    for item in data:
        out.append(aws_sdk_ebs.types.changed_block.deserialize_json(item))
    return out
