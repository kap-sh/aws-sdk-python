"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ConnectivityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rtbfabric.errors import DeserializationError

"""<p>The connectivity type for a link or gateway.</p>"""
ConnectivityType: TypeAlias = Literal[
    "DEFAULT",
    "PUBLIC_INGRESS",
    "PUBLIC_EGRESS",
    "EXTERNAL_INBOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "PUBLIC_INGRESS",
        "PUBLIC_EGRESS",
        "EXTERNAL_INBOUND",
    )
)


def serialize_json(value: ConnectivityType) -> str:
    return value


def deserialize_json(data: str) -> ConnectivityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectivityType value: {data!r}")
    return cast(ConnectivityType, data)
