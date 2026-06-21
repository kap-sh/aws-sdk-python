"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#HostedZoneAssociationStatus``."""

from typing import Literal, TypeAlias, cast

HostedZoneAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "OPERATIONAL",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: HostedZoneAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> HostedZoneAssociationStatus:
    return cast(HostedZoneAssociationStatus, data)
