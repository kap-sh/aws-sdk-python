"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IpV4List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.ip_v4

IpV4List: TypeAlias = list[
    "aws_sdk_license_manager_user_subscriptions.types.ip_v4.IpV4"
]


# --- restJson1 ser/de ---
def serialize_json(value: IpV4List) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV4List:
    return list(data)
