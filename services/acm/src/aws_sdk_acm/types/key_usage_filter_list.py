"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsageFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.key_usage_name

KeyUsageFilterList: TypeAlias = list["aws_sdk_acm.types.key_usage_name.KeyUsageName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsageFilterList) -> list:
    import aws_sdk_acm.types.key_usage_name

    out: list = []
    for item in value:
        out.append(aws_sdk_acm.types.key_usage_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyUsageFilterList:
    import aws_sdk_acm.types.key_usage_name

    out: KeyUsageFilterList = []
    for item in data:
        out.append(aws_sdk_acm.types.key_usage_name.deserialize_aws_json_1_1(item))
    return out
