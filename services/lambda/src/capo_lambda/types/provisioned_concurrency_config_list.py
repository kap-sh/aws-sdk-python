"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.provisioned_concurrency_config_list_item

ProvisionedConcurrencyConfigList: TypeAlias = list[
    "capo_lambda.types.provisioned_concurrency_config_list_item.ProvisionedConcurrencyConfigListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedConcurrencyConfigList) -> list:
    import capo_lambda.types.provisioned_concurrency_config_list_item

    out: list = []
    for item in value:
        out.append(
            capo_lambda.types.provisioned_concurrency_config_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProvisionedConcurrencyConfigList:
    import capo_lambda.types.provisioned_concurrency_config_list_item

    out: ProvisionedConcurrencyConfigList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_lambda.types.provisioned_concurrency_config_list_item.deserialize_json(
                item
            )
        )
    return out
