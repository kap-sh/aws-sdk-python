"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.instance

InstanceList: TypeAlias = list[
    "aws_sdk_license_manager_linux_subscriptions.types.instance.Instance"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceList) -> list:
    import aws_sdk_license_manager_linux_subscriptions.types.instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager_linux_subscriptions.types.instance.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InstanceList:
    import aws_sdk_license_manager_linux_subscriptions.types.instance

    out: InstanceList = []
    for item in data:
        out.append(
            aws_sdk_license_manager_linux_subscriptions.types.instance.deserialize_json(
                item
            )
        )
    return out
