"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_field

ServiceFieldList: TypeAlias = list["aws_sdk_ecs.types.service_field.ServiceField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceFieldList) -> list:
    import aws_sdk_ecs.types.service_field

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.service_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceFieldList:
    import aws_sdk_ecs.types.service_field

    out: ServiceFieldList = []
    for item in data:
        out.append(aws_sdk_ecs.types.service_field.deserialize_aws_json_1_1(item))
    return out
