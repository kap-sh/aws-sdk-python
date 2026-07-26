"""Generated from Smithy shape ``com.amazonaws.wafv2#IPAddresses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wafv2.types.ip_address

IPAddresses: TypeAlias = list["capo_wafv2.types.ip_address.IPAddress"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPAddresses) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IPAddresses:
    return list(data)
