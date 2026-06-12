"""Generated from Smithy shape ``com.amazonaws.acm#DomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_acm.types.domain_name_string

DomainList: TypeAlias = list["aws_sdk_acm.types.domain_name_string.DomainNameString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DomainList:
    return list(data)
