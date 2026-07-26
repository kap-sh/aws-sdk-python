"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#InstanceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager_linux_subscriptions.types.instance

InstanceList: TypeAlias = list[
    "capo_license_manager_linux_subscriptions.types.instance.Instance"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceList) -> list:
    import capo_license_manager_linux_subscriptions.types.instance

    out: list = []
    for item in value:
        out.append(
            capo_license_manager_linux_subscriptions.types.instance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InstanceList:
    import capo_license_manager_linux_subscriptions.types.instance

    out: InstanceList = []
    for item in data:
        out.append(
            capo_license_manager_linux_subscriptions.types.instance.deserialize_json(
                item
            )
        )
    return out
