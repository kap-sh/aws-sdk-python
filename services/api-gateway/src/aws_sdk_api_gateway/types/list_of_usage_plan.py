"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfUsagePlan``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.usage_plan

ListOfUsagePlan: TypeAlias = list["aws_sdk_api_gateway.types.usage_plan.UsagePlan"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUsagePlan) -> list:
    import aws_sdk_api_gateway.types.usage_plan

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.usage_plan.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfUsagePlan:
    import aws_sdk_api_gateway.types.usage_plan

    out: ListOfUsagePlan = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.usage_plan.deserialize_json(item))
    return out
