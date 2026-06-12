"""Generated from Smithy shape ``com.amazonaws.wafv2#AsnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.asn

AsnList: TypeAlias = list["aws_sdk_wafv2.types.asn.ASN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AsnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AsnList:
    return list(data)
