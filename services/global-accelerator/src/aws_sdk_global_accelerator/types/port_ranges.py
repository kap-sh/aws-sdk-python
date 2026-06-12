"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_range

PortRanges: TypeAlias = list["aws_sdk_global_accelerator.types.port_range.PortRange"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortRanges) -> list:
    import aws_sdk_global_accelerator.types.port_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.port_range.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PortRanges:
    import aws_sdk_global_accelerator.types.port_range

    out: PortRanges = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.port_range.deserialize_aws_json_1_1(item)
        )
    return out
