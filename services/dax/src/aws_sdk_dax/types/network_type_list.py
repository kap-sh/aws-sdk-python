"""Generated from Smithy shape ``com.amazonaws.dax#NetworkTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dax.types.network_type

NetworkTypeList: TypeAlias = list["aws_sdk_dax.types.network_type.NetworkType"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkTypeList) -> list:
    import aws_sdk_dax.types.network_type

    out: list = []
    for item in value:
        out.append(aws_sdk_dax.types.network_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkTypeList:
    import aws_sdk_dax.types.network_type

    out: NetworkTypeList = []
    for item in data:
        out.append(aws_sdk_dax.types.network_type.deserialize_aws_json_1_1(item))
    return out
