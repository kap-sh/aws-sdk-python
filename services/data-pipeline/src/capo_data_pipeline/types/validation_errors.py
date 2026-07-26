"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.validation_error

ValidationErrors: TypeAlias = list[
    "capo_data_pipeline.types.validation_error.ValidationError"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationErrors) -> list:
    import capo_data_pipeline.types.validation_error

    out: list = []
    for item in value:
        out.append(
            capo_data_pipeline.types.validation_error.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ValidationErrors:
    import capo_data_pipeline.types.validation_error

    out: ValidationErrors = []
    for item in data:
        out.append(
            capo_data_pipeline.types.validation_error.deserialize_aws_json_1_1(item)
        )
    return out
