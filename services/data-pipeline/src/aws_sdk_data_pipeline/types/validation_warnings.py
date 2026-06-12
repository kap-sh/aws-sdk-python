"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.validation_warning

ValidationWarnings: TypeAlias = list[
    "aws_sdk_data_pipeline.types.validation_warning.ValidationWarning"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationWarnings) -> list:
    import aws_sdk_data_pipeline.types.validation_warning

    out: list = []
    for item in value:
        out.append(
            aws_sdk_data_pipeline.types.validation_warning.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ValidationWarnings:
    import aws_sdk_data_pipeline.types.validation_warning

    out: ValidationWarnings = []
    for item in data:
        out.append(
            aws_sdk_data_pipeline.types.validation_warning.deserialize_aws_json_1_1(
                item
            )
        )
    return out
