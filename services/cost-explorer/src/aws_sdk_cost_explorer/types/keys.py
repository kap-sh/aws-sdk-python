"""Generated from Smithy shape ``com.amazonaws.costexplorer#Keys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.key

Keys: TypeAlias = list["aws_sdk_cost_explorer.types.key.Key"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Keys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> Keys:
    return list(data)
