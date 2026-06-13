"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.subnet

Subnets: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.subnet.Subnet"
]


# --- restJson1 ser/de ---
def serialize_json(value: Subnets) -> list:
    return list(value)


def deserialize_json(data: list) -> Subnets:
    return list(data)
