"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#TagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.tag_key

TagKeys: TypeAlias = list["aws_sdk_route53globalresolver.types.tag_key.TagKey"]


# --- restJson1 ser/de ---
def serialize_json(value: TagKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> TagKeys:
    return list(data)
