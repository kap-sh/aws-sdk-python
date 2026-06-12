"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfUsagePlanKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.usage_plan_key

ListOfUsagePlanKey: TypeAlias = list[
    "aws_sdk_api_gateway.types.usage_plan_key.UsagePlanKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUsagePlanKey) -> list:
    import aws_sdk_api_gateway.types.usage_plan_key

    out: list = []
    for item in value:
        out.append(aws_sdk_api_gateway.types.usage_plan_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfUsagePlanKey:
    import aws_sdk_api_gateway.types.usage_plan_key

    out: ListOfUsagePlanKey = []
    for item in data:
        out.append(aws_sdk_api_gateway.types.usage_plan_key.deserialize_json(item))
    return out
