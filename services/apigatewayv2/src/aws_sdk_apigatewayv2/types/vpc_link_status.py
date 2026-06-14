"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#VpcLinkStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apigatewayv2.errors import DeserializationError

"""<p>The status of the VPC link.</p>"""
VpcLinkStatus: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "FAILED",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "AVAILABLE",
        "DELETING",
        "FAILED",
        "INACTIVE",
    )
)


def serialize_json(value: VpcLinkStatus) -> str:
    return value


def deserialize_json(data: str) -> VpcLinkStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VpcLinkStatus value: {data!r}")
    return cast(VpcLinkStatus, data)
