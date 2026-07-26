"""Generated from Smithy shape ``com.amazonaws.support#ServiceCodeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_support.types.service_code2

ServiceCodeList: TypeAlias = list["capo_support.types.service_code2.ServiceCode2"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCodeList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServiceCodeList:
    return list(data)
