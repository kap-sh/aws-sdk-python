"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ConnectivityType``."""

from typing import Literal, TypeAlias, cast

"""<p>The connectivity type for a link or gateway.</p>"""
ConnectivityType: TypeAlias = Literal[
    "DEFAULT",
    "PUBLIC_INGRESS",
    "PUBLIC_EGRESS",
    "EXTERNAL_INBOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectivityType) -> str:
    return value


def deserialize_json(data: str) -> ConnectivityType:
    return cast(ConnectivityType, data)
