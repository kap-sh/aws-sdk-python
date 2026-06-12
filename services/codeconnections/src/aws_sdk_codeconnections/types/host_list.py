"""Generated from Smithy shape ``com.amazonaws.codeconnections#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.host

HostList: TypeAlias = list["aws_sdk_codeconnections.types.host.Host"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostList) -> list:
    import aws_sdk_codeconnections.types.host

    out: list = []
    for item in value:
        out.append(aws_sdk_codeconnections.types.host.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HostList:
    import aws_sdk_codeconnections.types.host

    out: HostList = []
    for item in data:
        out.append(aws_sdk_codeconnections.types.host.deserialize_aws_json_1_0(item))
    return out
