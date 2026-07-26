"""Generated from Smithy shape ``com.amazonaws.datapipeline#ValidationWarnings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_data_pipeline.types.validation_warning

ValidationWarnings: TypeAlias = list[
    "capo_data_pipeline.types.validation_warning.ValidationWarning"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidationWarnings) -> list:
    import capo_data_pipeline.types.validation_warning

    out: list = []
    for item in value:
        out.append(
            capo_data_pipeline.types.validation_warning.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ValidationWarnings:
    import capo_data_pipeline.types.validation_warning

    out: ValidationWarnings = []
    for item in data:
        out.append(
            capo_data_pipeline.types.validation_warning.deserialize_aws_json_1_1(item)
        )
    return out
