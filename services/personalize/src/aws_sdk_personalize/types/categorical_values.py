"""Generated from Smithy shape ``com.amazonaws.personalize#CategoricalValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.categorical_value

CategoricalValues: TypeAlias = list[
    "aws_sdk_personalize.types.categorical_value.CategoricalValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CategoricalValues:
    return list(data)
