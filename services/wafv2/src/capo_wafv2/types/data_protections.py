"""Generated from Smithy shape ``com.amazonaws.wafv2#DataProtections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.data_protection

DataProtections: TypeAlias = list["capo_wafv2.types.data_protection.DataProtection"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProtections) -> list:
    import capo_wafv2.types.data_protection

    out: list = []
    for item in value:
        out.append(capo_wafv2.types.data_protection.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DataProtections:
    import capo_wafv2.types.data_protection

    out: DataProtections = []
    for item in data:
        out.append(capo_wafv2.types.data_protection.deserialize_aws_json_1_1(item))
    return out
