"""Generated from Smithy shape ``com.amazonaws.outposts#outpostListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.outpost

outpostListDefinition: TypeAlias = list["aws_sdk_outposts.types.outpost.Outpost"]


# --- restJson1 ser/de ---
def serialize_json(value: outpostListDefinition) -> list:
    import aws_sdk_outposts.types.outpost

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.outpost.serialize_json(item))
    return out


def deserialize_json(data: list) -> outpostListDefinition:
    import aws_sdk_outposts.types.outpost

    out: outpostListDefinition = []
    for item in data:
        out.append(aws_sdk_outposts.types.outpost.deserialize_json(item))
    return out
