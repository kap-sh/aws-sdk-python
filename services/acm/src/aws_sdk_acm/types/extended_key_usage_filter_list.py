"""Generated from Smithy shape ``com.amazonaws.acm#ExtendedKeyUsageFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.extended_key_usage_name

ExtendedKeyUsageFilterList: TypeAlias = list[
    "aws_sdk_acm.types.extended_key_usage_name.ExtendedKeyUsageName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsageFilterList) -> list:
    import aws_sdk_acm.types.extended_key_usage_name

    out: list = []
    for item in value:
        out.append(
            aws_sdk_acm.types.extended_key_usage_name.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExtendedKeyUsageFilterList:
    import aws_sdk_acm.types.extended_key_usage_name

    out: ExtendedKeyUsageFilterList = []
    for item in data:
        out.append(
            aws_sdk_acm.types.extended_key_usage_name.deserialize_aws_json_1_1(item)
        )
    return out
