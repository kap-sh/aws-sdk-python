"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#FirewallBlockResponse``."""

from typing import Literal, TypeAlias, cast

FirewallBlockResponse: TypeAlias = Literal[
    "NODATA",
    "NXDOMAIN",
    "OVERRIDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallBlockResponse) -> str:
    return value


def deserialize_json(data: str) -> FirewallBlockResponse:
    return cast(FirewallBlockResponse, data)
