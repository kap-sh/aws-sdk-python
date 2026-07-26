"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsageFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_acm.types.key_usage_name

KeyUsageFilterList: TypeAlias = list["capo_acm.types.key_usage_name.KeyUsageName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsageFilterList) -> list:
    import capo_acm.types.key_usage_name

    out: list = []
    for item in value:
        out.append(capo_acm.types.key_usage_name.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> KeyUsageFilterList:
    import capo_acm.types.key_usage_name

    out: KeyUsageFilterList = []
    for item in data:
        out.append(capo_acm.types.key_usage_name.deserialize_aws_json_1_1(item))
    return out
