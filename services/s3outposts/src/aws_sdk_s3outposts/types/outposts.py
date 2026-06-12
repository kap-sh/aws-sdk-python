"""Generated from Smithy shape ``com.amazonaws.s3outposts#Outposts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_s3outposts.types.outpost

Outposts: TypeAlias = list["aws_sdk_s3outposts.types.outpost.Outpost"]


# --- restJson1 ser/de ---
def serialize_json(value: Outposts) -> list:
    import aws_sdk_s3outposts.types.outpost

    out: list = []
    for item in value:
        out.append(aws_sdk_s3outposts.types.outpost.serialize_json(item))
    return out


def deserialize_json(data: list) -> Outposts:
    import aws_sdk_s3outposts.types.outpost

    out: Outposts = []
    for item in data:
        out.append(aws_sdk_s3outposts.types.outpost.deserialize_json(item))
    return out
