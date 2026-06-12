"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#IpV6List``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.ip_v6

IpV6List: TypeAlias = list["aws_sdk_license_manager_user_subscriptions.types.ip_v6.IpV6"]


# --- restJson1 ser/de ---
def serialize_json(value: IpV6List) -> list:
    return list(value)


def deserialize_json(data: list) -> IpV6List:
    return list(data)