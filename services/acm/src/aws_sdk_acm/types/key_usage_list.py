"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.key_usage

KeyUsageList: TypeAlias = list["aws_sdk_acm.types.key_usage.KeyUsage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsageList) -> list:
    import aws_sdk_acm.types.key_usage

    out: list = []
    for item in value:
        out.append(aws_sdk_acm.types.key_usage.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyUsageList:
    import aws_sdk_acm.types.key_usage

    out: KeyUsageList = []
    for item in data:
        out.append(aws_sdk_acm.types.key_usage.deserialize_aws_json_1_1(item))
    return out
