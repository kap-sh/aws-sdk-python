"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#BlockOverrideDnsQueryType``."""

from typing import Literal, TypeAlias, cast

BlockOverrideDnsQueryType: TypeAlias = Literal["CNAME",]


# --- restJson1 ser/de ---
def serialize_json(value: BlockOverrideDnsQueryType) -> str:
    return value


def deserialize_json(data: str) -> BlockOverrideDnsQueryType:
    return cast(BlockOverrideDnsQueryType, data)
