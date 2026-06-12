"""Generated from Smithy shape ``com.amazonaws.batch#ShareAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.share_attributes

ShareAttributesList: TypeAlias = list[
    "aws_sdk_batch.types.share_attributes.ShareAttributes"
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareAttributesList) -> list:
    import aws_sdk_batch.types.share_attributes

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.share_attributes.serialize_json(item))
    return out


def deserialize_json(data: list) -> ShareAttributesList:
    import aws_sdk_batch.types.share_attributes

    out: ShareAttributesList = []
    for item in data:
        out.append(aws_sdk_batch.types.share_attributes.deserialize_json(item))
    return out
