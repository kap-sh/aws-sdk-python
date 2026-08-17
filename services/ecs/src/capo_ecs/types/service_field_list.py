"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_field

ServiceFieldList: TypeAlias = list["capo_ecs.types.service_field.ServiceField"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceFieldList) -> list:
    import capo_ecs.types.service_field

    out: list = []
    for item in value:
        out.append(capo_ecs.types.service_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceFieldList:
    import capo_ecs.types.service_field

    out: ServiceFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.service_field.deserialize_aws_json_1_1(item))
    return out
