"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ByoipCidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.byoip_cidr

ByoipCidrs: TypeAlias = list["aws_sdk_global_accelerator.types.byoip_cidr.ByoipCidr"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByoipCidrs) -> list:
    import aws_sdk_global_accelerator.types.byoip_cidr

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.byoip_cidr.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ByoipCidrs:
    import aws_sdk_global_accelerator.types.byoip_cidr

    out: ByoipCidrs = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.byoip_cidr.deserialize_aws_json_1_1(item)
        )
    return out
