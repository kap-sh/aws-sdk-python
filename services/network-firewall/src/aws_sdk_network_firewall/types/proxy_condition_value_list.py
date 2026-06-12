"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ProxyConditionValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.proxy_condition_value

ProxyConditionValueList: TypeAlias = list[
    "aws_sdk_network_firewall.types.proxy_condition_value.ProxyConditionValue"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProxyConditionValueList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProxyConditionValueList:
    return list(data)
