"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpSets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.ip_set

IpSets: TypeAlias = list["aws_sdk_global_accelerator.types.ip_set.IpSet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpSets) -> list:
    import aws_sdk_global_accelerator.types.ip_set

    out: list = []
    for item in value:
        out.append(aws_sdk_global_accelerator.types.ip_set.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpSets:
    import aws_sdk_global_accelerator.types.ip_set

    out: IpSets = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.ip_set.deserialize_aws_json_1_1(item)
        )
    return out
