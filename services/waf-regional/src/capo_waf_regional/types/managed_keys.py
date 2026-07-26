"""Generated from Smithy shape ``com.amazonaws.wafregional#ManagedKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_waf_regional.types.managed_key

ManagedKeys: TypeAlias = list["capo_waf_regional.types.managed_key.ManagedKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ManagedKeys:
    return list(data)
