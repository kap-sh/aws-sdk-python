"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionsByCapacityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_versions_by_capacity_provider_list_item

FunctionVersionsByCapacityProviderList: TypeAlias = list[
    "capo_lambda.types.function_versions_by_capacity_provider_list_item.FunctionVersionsByCapacityProviderListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionVersionsByCapacityProviderList) -> list:
    import capo_lambda.types.function_versions_by_capacity_provider_list_item

    out: list = []
    for item in value:
        out.append(
            capo_lambda.types.function_versions_by_capacity_provider_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FunctionVersionsByCapacityProviderList:
    import capo_lambda.types.function_versions_by_capacity_provider_list_item

    out: FunctionVersionsByCapacityProviderList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda.types.function_versions_by_capacity_provider_list_item.deserialize_json(
                item
            )
        )
    return out
