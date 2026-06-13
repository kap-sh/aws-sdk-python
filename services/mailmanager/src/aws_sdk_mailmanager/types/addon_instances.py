"""Generated from Smithy shape ``com.amazonaws.mailmanager#AddonInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.addon_instance

AddonInstances: TypeAlias = list[
    "aws_sdk_mailmanager.types.addon_instance.AddonInstance"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddonInstances) -> list:
    import aws_sdk_mailmanager.types.addon_instance

    out: list = []
    for item in value:
        out.append(
            aws_sdk_mailmanager.types.addon_instance.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AddonInstances:
    import aws_sdk_mailmanager.types.addon_instance

    out: AddonInstances = []
    for item in data:
        out.append(
            aws_sdk_mailmanager.types.addon_instance.deserialize_aws_json_1_0(item)
        )
    return out
