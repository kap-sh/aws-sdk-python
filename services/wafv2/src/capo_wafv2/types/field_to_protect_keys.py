"""Generated from Smithy shape ``com.amazonaws.wafv2#FieldToProtectKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.field_to_protect_key_name

FieldToProtectKeys: TypeAlias = list[
    "capo_wafv2.types.field_to_protect_key_name.FieldToProtectKeyName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldToProtectKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FieldToProtectKeys:
    return list(data)
