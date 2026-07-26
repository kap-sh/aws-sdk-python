"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListLineageEntityParameterKey``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.string_parameter_value

ListLineageEntityParameterKey: TypeAlias = list[
    "capo_sagemaker.types.string_parameter_value.StringParameterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLineageEntityParameterKey) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ListLineageEntityParameterKey:
    return list(data)
