"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#HostedZoneAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_route53globalresolver.errors import DeserializationError

HostedZoneAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "OPERATIONAL",
        "DELETING",
    )
)


def serialize_json(value: HostedZoneAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> HostedZoneAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown HostedZoneAssociationStatus value: {data!r}"
        )
    return cast(HostedZoneAssociationStatus, data)
