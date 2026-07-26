"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfUsagePlanKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.usage_plan_key

ListOfUsagePlanKey: TypeAlias = list[
    "capo_api_gateway.types.usage_plan_key.UsagePlanKey"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfUsagePlanKey) -> list:
    import capo_api_gateway.types.usage_plan_key

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.usage_plan_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfUsagePlanKey:
    import capo_api_gateway.types.usage_plan_key

    out: ListOfUsagePlanKey = []
    for item in data:
        out.append(capo_api_gateway.types.usage_plan_key.deserialize_json(item))
    return out
