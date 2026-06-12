"""Generated from Smithy shape ``com.amazonaws.personalize#IntegerHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.integer_hyper_parameter_range

IntegerHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.integer_hyper_parameter_range.IntegerHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegerHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.integer_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.integer_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IntegerHyperParameterRanges:
    import aws_sdk_personalize.types.integer_hyper_parameter_range

    out: IntegerHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.integer_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
