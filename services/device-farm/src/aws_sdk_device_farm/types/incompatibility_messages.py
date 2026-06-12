"""Generated from Smithy shape ``com.amazonaws.devicefarm#IncompatibilityMessages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.incompatibility_message

IncompatibilityMessages: TypeAlias = list[
    "aws_sdk_device_farm.types.incompatibility_message.IncompatibilityMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IncompatibilityMessages) -> list:
    import aws_sdk_device_farm.types.incompatibility_message

    out: list = []
    for item in value:
        out.append(
            aws_sdk_device_farm.types.incompatibility_message.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IncompatibilityMessages:
    import aws_sdk_device_farm.types.incompatibility_message

    out: IncompatibilityMessages = []
    for item in data:
        out.append(
            aws_sdk_device_farm.types.incompatibility_message.deserialize_aws_json_1_1(
                item
            )
        )
    return out
