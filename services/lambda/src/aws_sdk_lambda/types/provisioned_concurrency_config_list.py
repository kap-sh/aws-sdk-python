"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lambda.types.provisioned_concurrency_config_list_item

ProvisionedConcurrencyConfigList: TypeAlias = list[
    "aws_sdk_lambda.types.provisioned_concurrency_config_list_item.ProvisionedConcurrencyConfigListItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedConcurrencyConfigList) -> list:
    import aws_sdk_lambda.types.provisioned_concurrency_config_list_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lambda.types.provisioned_concurrency_config_list_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProvisionedConcurrencyConfigList:
    import aws_sdk_lambda.types.provisioned_concurrency_config_list_item

    out: ProvisionedConcurrencyConfigList = []
    for item in data:
        out.append(
            aws_sdk_lambda.types.provisioned_concurrency_config_list_item.deserialize_json(
                item
            )
        )
    return out
