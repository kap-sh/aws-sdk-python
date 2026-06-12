"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.access_key

AccessKeyList: TypeAlias = list["aws_sdk_lightsail.types.access_key.AccessKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessKeyList) -> list:
    import aws_sdk_lightsail.types.access_key

    out: list = []
    for item in value:
        out.append(aws_sdk_lightsail.types.access_key.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AccessKeyList:
    import aws_sdk_lightsail.types.access_key

    out: AccessKeyList = []
    for item in data:
        out.append(aws_sdk_lightsail.types.access_key.deserialize_aws_json_1_1(item))
    return out
