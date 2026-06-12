"""Generated from Smithy shape ``com.amazonaws.support#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_support.types.service

ServiceList: TypeAlias = list["aws_sdk_support.types.service.Service"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceList) -> list:
    import aws_sdk_support.types.service

    out: list = []
    for item in value:
        out.append(aws_sdk_support.types.service.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceList:
    import aws_sdk_support.types.service

    out: ServiceList = []
    for item in data:
        out.append(aws_sdk_support.types.service.deserialize_aws_json_1_1(item))
    return out
