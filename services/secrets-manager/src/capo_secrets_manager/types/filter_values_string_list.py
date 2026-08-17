"""Generated from Smithy shape ``com.amazonaws.secretsmanager#FilterValuesStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_secrets_manager.types.filter_value_string_type

FilterValuesStringList: TypeAlias = list[
    "capo_secrets_manager.types.filter_value_string_type.FilterValueStringType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterValuesStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> FilterValuesStringList:
    return [item for item in data if item is not None]
