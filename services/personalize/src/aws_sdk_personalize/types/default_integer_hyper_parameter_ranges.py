"""Generated from Smithy shape ``com.amazonaws.personalize#DefaultIntegerHyperParameterRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize.types.default_integer_hyper_parameter_range

DefaultIntegerHyperParameterRanges: TypeAlias = list[
    "aws_sdk_personalize.types.default_integer_hyper_parameter_range.DefaultIntegerHyperParameterRange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultIntegerHyperParameterRanges) -> list:
    import aws_sdk_personalize.types.default_integer_hyper_parameter_range

    out: list = []
    for item in value:
        out.append(
            aws_sdk_personalize.types.default_integer_hyper_parameter_range.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DefaultIntegerHyperParameterRanges:
    import aws_sdk_personalize.types.default_integer_hyper_parameter_range

    out: DefaultIntegerHyperParameterRanges = []
    for item in data:
        out.append(
            aws_sdk_personalize.types.default_integer_hyper_parameter_range.deserialize_aws_json_1_1(
                item
            )
        )
    return out
