"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_override

PortOverrides: TypeAlias = list[
    "aws_sdk_global_accelerator.types.port_override.PortOverride"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortOverrides) -> list:
    import aws_sdk_global_accelerator.types.port_override

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.port_override.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PortOverrides:
    import aws_sdk_global_accelerator.types.port_override

    out: PortOverrides = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.port_override.deserialize_aws_json_1_1(
                item
            )
        )
    return out
