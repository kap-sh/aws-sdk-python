"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AccessTokens``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53globalresolver.types.access_token_item

AccessTokens: TypeAlias = list[
    "aws_sdk_route53globalresolver.types.access_token_item.AccessTokenItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: AccessTokens) -> list:
    import aws_sdk_route53globalresolver.types.access_token_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53globalresolver.types.access_token_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AccessTokens:
    import aws_sdk_route53globalresolver.types.access_token_item

    out: AccessTokens = []
    for item in data:
        out.append(
            aws_sdk_route53globalresolver.types.access_token_item.deserialize_json(item)
        )
    return out
